#!/usr/bin/env python
# gene_names_from_chr21.py

"""This program takes a user provided gene name from
 a user-provided file and returns the description of the gene"""

import argparse
import sys
from assignment4 import io_utils


def main():
    """main section of gene_names_from_chr21.txt"""
    # get command line arguments
    args = get_cli_args()
    infile = args.infile
    fh_in = io_utils.get_filehandle(infile, "r")
    # create gene dictionary from input file
    gene_dict = create_gene_dict(fh_in)

    # ask for user input
    # exit system if quit is entered
    name_input = input('Enter gene name of interest. Type quit to exit: ')
    if name_input.casefold() == 'quit':
        sys.exit('Thanks for querying the data.')

    # print out gene name and description if valid
    if name_input in gene_dict:
        print(f'{name_input} found! Here is the description:')
        print(f'{gene_dict[name_input]}')

    else:
        print('Not a valid gene name.')

    fh_in.close()


def create_gene_dict(fh_in):
    """creates a dictionary of name and description out of the input file"""
    # initialize an empty dictionary to store key/value pairs
    gene_dict = {}

    # loop over each file in the input to create a dict for each
    for line in fh_in:
        line_parse = line.replace('\n', '').split('\t')
        name = line_parse[0]
        desc = line_parse[1]
        gene_dict[name] = desc

    return gene_dict


def get_cli_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Open chr21_genes.txt, and ask user for a gene name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the text file of gene names and descriptions
    parser.add_argument('-i', '--infile',
                        dest='infile',  # variable to access this data later: args.infile
                        help='assignment4/chr21_genes.txt',
                        default="chr21_genes.txt",
                        type=str,
                        required=True)

    return parser.parse_args()


if __name__ == "__main__":
    main()
