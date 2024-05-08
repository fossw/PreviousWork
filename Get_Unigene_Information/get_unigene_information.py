#!/usr/bin/env python
# get_unigene_information.py

"""This program takes in two command line arguments (host name and gene name)
and returns an index of which tissues that gene is expressed in for the provided host organism,
as well as a message with the number of gene occurrences. The organisms and
genes which can be used in this program are limited to those provided in the ggli_data directory."""

import argparse
import re
import sys
from ggli import config
from ggli import io_utils


def main():
    """This is the main section for the get_gene_level_information.py program"""
    # call arguments
    args = get_cli_args()
    host_name = args.HOST
    gene_file_name = args.GENE
    # update host name from provided name
    host_name_final = update_host_name(host_name)
    # return sorted tissue list for matching
    tissue_list_sorted = get_data_for_gene_file(gene_file_name)
    # print results
    print_host_to_gene_name_output(host_name_final, gene_file_name, tissue_list_sorted)


def get_cli_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Give the Host and Gene name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the unigene files of gene names and hosts
    parser.add_argument('--host',
                        dest='HOST',  # variable to access this data later: args.HOST
                        help='Name of Host',
                        default="Human",
                        required=False)

    parser.add_argument('-g', '--gene',
                        dest='GENE',  # variable to access this data later: args.GENE
                        help='Name of Gene',
                        default="TGM1",
                        required=False)

    return parser.parse_args()


def update_host_name(host_name):
    """retrieves a temporary host name from the configuration file"""

    # call host name dictionary from config.py
    # redirect each scientific name with an underscore to its common host name
    host_dict = config.get_keywords_for_hosts()
    if host_name == "Homo_sapiens":
        host_name = "human"
    if host_name == "Bos_taurus":
        host_name = "cow"
    if host_name == "Equus_caballus":
        host_name = "horse"
    if host_name == "Mus_musculus":
        host_name = "mouse"
    if host_name == "Ovis_aries":
        host_name = "sheep"
    if host_name == "Rattus_norvegicus":
        host_name = "rat"
    # convert each name to lowercase to remove case sensitivity
    host_name = host_name.lower()
    # return final host name if found in the config module dictionary
    if host_name in host_dict.keys():
        host_name_final = host_dict.get(host_name)
        return host_name_final
    else:
        # print viable directories if not found and exit the program
        _print_directories_for_hosts()
        sys.exit()


def _print_directories_for_hosts():
    """Gives a list of valid host names if the
    user-provided one is not in the host directory"""

    # differentiate between common vs scientific names
    host_name = config.get_keywords_for_hosts()
    common_list = sorted(list(host_name.keys()))
    scientific_list = tuple(set(host_name.values()))

    print("\nEither the Host Name you are searching for is not in the database")
    print("\nor If you are trying to use the scientific name please put the name in double quotes:")
    print('\n"Scientific name"')
    print("\nHere is a (non-case sensitive) list of available Hosts by scientific name")
    # print out possible host names for expression analysis
    for index, host_name in enumerate(sorted(scientific_list), 1):
        print(f"{index}. {host_name.capitalize()}")
    print("\nHere is a (non-case sensitive) list of available Hosts by common name")
    for index, host_name in enumerate(common_list, 1):
        print(f"{index}. {host_name.capitalize()}")


def get_data_for_gene_file(gene_file_name):
    """Retrieves list of tissues from gene file"""

    args = get_cli_args()
    host_name = args.HOST
    host_name_final = update_host_name(host_name)
    # get values from ggli.config.py
    file = "/".join((config.get_directory_for_unigene(),
                     host_name_final, gene_file_name + "." + config.get_extension_for_unigene()))
    fh_in = io_utils.get_filehandle(file, "r")
    # check for the existence of file
    if io_utils.is_gene_file_valid(file):
        # using f-strings
        print(f"\nFound Gene {gene_file_name} for {host_name_final}")
    else:
        print("Not found")
        print(f"Gene {gene_file_name} does not exist for {host_name}. exiting now...", file=sys.stderr)
        sys.exit(1)

    for line in fh_in:
        # match each gene with its EXPRESS section of the
        # unigene file wih regex to get a list of tissues
        match = re.search(r'^EXPRESS\s+(\D+)', line)
        if match:
            tissue_string = match.group(1)  # match here is an object. group1
            tissue_list = list(tissue_string.split(sep='|'))
            tissue_list_sorted = sorted([tissue.strip() for tissue in tissue_list])
            return tissue_list_sorted


def print_host_to_gene_name_output(host_name_final, gene_file_name, tissue_list_sorted):
    """Prints the number of tissues found
    from the previous match as well as an index of them"""
    # return list of tissues with the number expressed
    numb_tissues = len(tissue_list_sorted)
    print(f"In {host_name_final}, There are {numb_tissues} tissues that {gene_file_name} is expressed in:\n")
    # print final output
    for index, i in enumerate(tissue_list_sorted, 1):
        print(f"{index}. {i.capitalize()}")


if __name__ == "__main__":
    main()
