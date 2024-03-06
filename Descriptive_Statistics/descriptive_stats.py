#!/usr/bin/env python
# descriptive_stats.py

"""This program takes a user provided dataset as input
and calculates the descriptive statistics of a user-specified column"""

import sys
import math


def data_loop(file_name, column_to_parse):
    """This function opens a file provided by the user and parses a
    column specified by the user.
    It returns a list of numbers and a line count"""

    # initialize list to store floats in
    numb_list = []
    # initialize an empty list for invalid numbers/characters
    inval_list = []
    # initialize line count
    count_line = 1

    # open file and loop over data
    with open(file_name, 'r') as infile:
        for count_line, line in enumerate(infile, start=1):
            # split the lines to user specification
            try:
                numb = line.split("\t")[column_to_parse]
                # store non-float values in separate list
                if numb == "NaN":
                    inval_list.append(numb)
                else:
                    numb_list.append(float(numb))
            # raise exceptions for invalid list indexes and strings
            except ValueError:
                print(f"Skipping line number {count_line}:"
                      f" could not convert string to float: '{numb}'")
            # exit program if no valid list indexes
            except IndexError:
                sys.exit(f"Exiting: There is no valid 'list index' "
                         f"in column {column_to_parse} in line 1 in file: {file_name}")
        # calculate descriptive statistics for returned number list
        calculate_stats(numb_list, count_line)
        return count_line, inval_list, numb_list

def calculate_stats(numb_list, count_line):
    """This function calculates and prints out
     the descriptive statistics for a list of numbers"""

    # calculation for median
    numbers = sorted(numb_list)
    numbs_length = len(numbers) // 2
    numbs_med = numbers[numbs_length]
    if len(numbers) % 2 == 0:
        numbs_med = (numbs_med + numbers[numbs_length - 1]) / 2

    # assign variables to all statistics
    count_numb = count_line
    validnum = len(numb_list)
    avg_stats = sum(numb_list) / len(numb_list)
    var_stats = variance_calc(numb_list)
    stdv_stats = math.sqrt(var_stats)
    med_stats = numbs_med
    max_stats = max(numb_list)
    min_stats = min(numb_list)

    # print the formatted calculations
    print(f"    Column: {COLUMN_TO_PARSE}")
    print(f"""
        Count     =   {count_numb:.3f}
        ValidNum  =   {validnum:.3f}
        Average   =    {avg_stats:.3f}
        Maximum   =    {max_stats:.3f}
        Minimum   =    {min_stats:.3f}
        Variance  =    {var_stats:.3f}
        Std Dev   =    {stdv_stats:.3f}
        Median    =    {med_stats:.3f}  """)

    return avg_stats, var_stats, stdv_stats, med_stats, max_stats, min_stats

def variance_calc(numb_list):
    """This function calculates the variance of
    a dataset from a returned list of valid numbers"""

    numbs_length = len(numb_list)
    numbs_mean = sum(numb_list) / numbs_length
    var_calc = sum((numb - numbs_mean) ** 2 for numb in numb_list) / (numbs_length - 1)

    return var_calc

if __name__ == "__main__":
    FILE_NAME = sys.argv[1]
    COLUMN_TO_PARSE = int(sys.argv[2])
    data_loop(FILE_NAME, COLUMN_TO_PARSE)
