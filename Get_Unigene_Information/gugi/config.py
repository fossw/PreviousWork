#!/usr/bin/env python
# config.py

"""Configures data file and unigene information for the main program"""

_DIRECTORY_FOR_UNIGENE = "./ggli_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    """Returns the directory path for the file"""

    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """Returns the extension for the unigene file"""

    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts():
    """Creates a dictionary of scientific name pairs with their common names"""

    homo_sapiens = "Homo_sapiens"
    bos_taurus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_dict = {"human": homo_sapiens,
                 "humans": homo_sapiens,
                 "homo sapiens": homo_sapiens,
                 "bos taurus": bos_taurus,
                 "cow": bos_taurus,
                 "cows": bos_taurus,
                 "equus caballus": equus_caballus,
                 "horse": equus_caballus,
                 "horses": equus_caballus,
                 "mus musculus": mus_musculus,
                 "mouse": mus_musculus,
                 "mice": mus_musculus,
                 "ovis aries": ovis_aries,
                 "sheep": ovis_aries,
                 "sheeps": ovis_aries,
                 "rattus norvegicus": rattus_norvegicus,
                 "rat": rattus_norvegicus,
                 "rats": rattus_norvegicus}

    return host_dict


def get_error_string_4_file_not_found_error(file: str) -> None:
    """Prints error message if FileNotFoundError for given file"""
    print(f"Invalid argument for file: {file}")


def get_error_string_4_value_error() -> None:
    """Prints line for value error"""
    print(f"This value is an invalid argument")


def get_error_string_4_typeerror():
    """Raise value error if incorrect value given"""
    print(f"Invalid Type passed in: ")
