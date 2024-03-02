#!/usr/bin/env python
# find_common_cats.py

"""This program counts how many genes are in each category based on the categories
 listed in the chr21_genes_categories.txt and prints the output in a separate file"""

import argparse
from assignment4 import io_utils


def main():
    """main section for find_common_cats.py"""

    # get arguments
    args = get_cli_args()
    infile1 = args.INFILE1
    infile2 = args.INFILE2
    # read user-provided input files
    fh_in1 = io_utils.get_filehandle(infile1, "r")
    fh_in2 = io_utils.get_filehandle(infile2, "r")
    # write file for output
    fh_out = io_utils.get_filehandle("OUTPUT/categories.txt", "w")
    sorted_cats_dic = find_common_cats(fh_in1)
    descriptions = find_descriptions(fh_in2)
    # print results to output
    print_results(descriptions, sorted_cats_dic, fh_out)
    fh_in1.close()
    fh_in2.close()
    fh_out.close()


def get_cli_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Combine on gene name and count the category occurrence",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the user-provided text files
    parser.add_argument('-i1', '--INFILE1',
                        dest='INFILE1',  # variable to access this data later: args.infile
                        help='assignment4/chr21_genes.txt',
                        default="chr21_genes.txt",
                        type=str,
                        required=True)

    parser.add_argument('-i2', '--INFILE2',
                        dest='INFILE2',  # variable to access this data later: args.infile
                        help='assignment4/chr21_genes_categories.txt',
                        default="chr21_genes_categories.txt",
                        type=str,
                        required=True)

    return parser.parse_args()


def find_common_cats(fh_in):
    """This function creates a dictionary of categories from the input file and counts
     how many are similar. A numerically sorted dictionary is returned"""

    # initialize empty dictionary
    cats_dic = {}

    for line in fh_in:
        parsed_line = line.replace('\n', '').split('\t')
        cats = parsed_line[2]

        # add one to the count if the category is seen again
        if cats in cats_dic:
            cats_dic[cats] += 1
        else:
            cats_dic[cats] = 1

    # sort dictionary
    sorted_cats_dic = sorted(cats_dic.items())

    return dict(sorted_cats_dic)


def find_descriptions(fh_in2):
    """This function separates the descriptions from the
     second input file and returns them in a dictionary"""

    # initialize empty dictionary
    desc_dic = {}

    # store descriptions in empty dictionary
    for line in fh_in2:
        parsed_line = line.replace('\n', '').split('\t')
        cats = parsed_line[0]
        desc = parsed_line[1]
        desc_dic[cats] = desc

    return desc_dic


def print_results(descriptions, sorted_cats_dic, fh_out):
    """This function sends the categories seen,
    count in each category, and corresponding descriptions in"""

    # create headers for output file
    print("Category", "\t", "Occurrence", "\t", "Description", "\n", file=fh_out)

    # loop over the keys and values in both returned dictionaries
    for key1, val1 in sorted_cats_dic.items():
        for key2, val2 in descriptions.items():
            # only send to file if the category matches the description
            if key1 == key2:
                print(f"{key1}\t\t\t{val1}\t\t\t{val2}", file=fh_out)


if __name__ == "__main__":
    main()
