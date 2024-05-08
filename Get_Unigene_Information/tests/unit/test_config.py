#!/usr/bin/env python
# test_config.py

"""Runs various tests on config from ggli to check for proper configuration"""


from assignment5 import config

FILE_TO_TEST = "test_file.txt"


def test_get_error_string_4_value_error():
    """Tests if a value error will print with an incorrect value passed"""
    # tests for value error message
    config.get_error_string_4_value_error()


def test_get_file_keywords():
    """tests if function can
    accurately ket keywords from the config dictionary"""
    # tests two random species entries
    test_dic = config.get_keywords_for_hosts()
    assert test_dic.get("sheep") == "Ovis_aries"
    assert test_dic.get("human") == "Homo_sapiens"
    assert len(test_dic.keys()) == 18


def get_error_string_4_typeerror():
    """Raise value error if incorrect value given"""
    # Prints error
    print(f"Invalid Type passed in: ")


def _create_file_for_testing(file):
    """creates file for testing"""
    # creates a file for testing
    open(file, "w").close()
