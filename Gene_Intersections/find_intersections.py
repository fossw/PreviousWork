#!/usr/bin/env python
# intersection_of_gene_names.py


"""This program finds the intersection of gene names in two given files"""

import argparse
from assignment4 import io_utils


def main():
    """main section for intersection_of_gene_names.py"""
    # get command line input
    args = get_cli_args()
    infile1 = args.INFILE1
    infile2 = args.INFILE2
    fh_in1 = io_utils.get_filehandle(infile1, 'r')
    fh_in2 = io_utils.get_filehandle(infile2, 'r')
    fh_out = io_utils.get_filehandle("OUTPUT/intersection_output.txt", "w")
    # get a list og gene names from each file
    chr21_names, hugo_names = get_gene_names(fh_in1, fh_in2)
    # get sets of names from both returned lists with unique names
    unames_chr21, unames_hugo = get_unique_names(chr21_names, hugo_names)
    # get common names and write to output file
    common_names = get_intersection(unames_chr21, unames_hugo, fh_out)
    # print to standard out
    print_results(unames_chr21, unames_hugo, common_names)
    # close files
    fh_in1.close()
    fh_in2.close()
    fh_out.close()


def get_cli_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Provide two gene list (ignore header line), find intersection",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the text files of gene names
    parser.add_argument('-i1', '--INFILE1',
                        dest='INFILE1',  # variable to access this data later: args.infile
                        help='Gene list 1 to open',
                        default="chr21_genes.txt",
                        type=str,
                        required=True)

    parser.add_argument('-i2', '--INFILE2',
                        dest='INFILE2',  # variable to access this data later: args.infile
                        help='Gene list 2 to open',
                        default="HUGO_genes.txt",
                        type=str,
                        required=True)

    return parser.parse_args()


def get_gene_names(fh_in1, fh_in2):
    """This function retrieves a list of gene names from both input files given"""
    # initialize two empty lists for each file
    chr21_names = []
    hugo_names = []

    # loop over each file to retrieve the names from each line
    for line in fh_in1:
        line_parsed = line.replace('\n', '').split('\t')
        names = line_parsed[0]
        chr21_names.append(names)

    for line in fh_in2:
        line_parsed = line.replace('\n', '').split('\t')
        names = line_parsed[0]
        hugo_names.append(names)

    return chr21_names, hugo_names


def get_unique_names(chr21_names, hugo_names):
    """This function creates sets out of the returned
     lists to later retrieve their unique and common names"""

    # create sets out of the return lists to store multiple items
    unames_chr21 = list(set(chr21_names))
    unames_hugo = list(set(hugo_names))

    return unames_hugo, unames_chr21


def get_intersection(unames_chr21, unames_hugo, fh_out):
    """This function finds the intersection between the two returned sets,
     and their list of common names"""

    # create intersection between both sets of unique names
    intersection = set(unames_chr21).intersection(unames_hugo)
    # use sorted function to sort alphabetically
    common_names = sorted(list(intersection))

    for name in common_names:
        print(name, file=fh_out)

    return common_names


def print_results(unames_chr21, unames_hugo, common_names):
    """this function prints results to stdout"""

    # convert lists to integer values
    chr21_int = len(unames_chr21)
    hugo_int = len(unames_hugo)
    common_int = len(common_names)

    # print integer result values to stdout
    print(f"Number of unique gene names in chr21_genes.txt: {chr21_int}")
    print(f"Number of unique gene names in HUGO_genes.txt: {hugo_int}")
    print(f"Number of common gene symbols found: {common_int}")
    print("Output stored in OUTPUT/intersection_output.txt")


if __name__ == "__main__":
    main()
