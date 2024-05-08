#!/usr/bin/env python
# io_utils.py

"""Utilized this function to retrieve filehandles for reading or writing"""

import os


def get_filehandle(infile, mode):
    """Opens and reads the given file"""

    # open infile and return file handle (close later)
    try:
        file_handle = open(infile, mode)
        return file_handle
    # raise OSError if file doesn't exist
    except OSError:
        print(f"Couldn't open {infile} due to OSError")
        raise
    # raise ValueError if invalid file
    except ValueError:
        print(f"Couldn't open {infile} due to ValueError")
        raise


def is_gene_file_valid(infile):
    """determines if the OS path exists, returns False if it doesn't"""
    # use os path to get the infile
    if os.path.exists(infile):
        return True
    else:
        return False
