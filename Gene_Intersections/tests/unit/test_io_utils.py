#!/usr/bin/env python
# test_io_utils.py

"""Runs various tests on io_utils from assignment4 to check for proper function"""

import os
import pytest
from assignment4 import io_utils


FILE_TO_READ = "test_file.txt"


def test_io_utils_for_reading():
    """tests to see if file can be read"""
    # does it open a file for reading?
    # test
    _create_file_for_testing(FILE_TO_READ)
    test = io_utils.get_filehandle(FILE_TO_READ, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"
    test.close()
    os.remove(FILE_TO_READ)


def test_io_utils_for_writing():
    """tests to see if file can be written"""
    # does it open a file for writing?
    # test

    test = io_utils.get_filehandle(FILE_TO_READ, "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove(FILE_TO_READ)


def test_valueerror():
    """tests for ValueError"""
    # Tests an ValueError for non-existent file
    # test
    _create_file_for_testing(FILE_TO_READ)
    with pytest.raises(ValueError):
        io_utils.get_filehandle("does_not_exist.txt", "rrr")
    os.remove(FILE_TO_READ)


def test_oserror():
    """tests for OSError"""
    # Tests an OSError for non-existent file
    # test
    with pytest.raises(OSError):
        io_utils.get_filehandle("file_not_here.txt", "r")


def _create_file_for_testing(file):
    """creates file for testing"""
    # creates a file for testing
    open(file, "w").close()
