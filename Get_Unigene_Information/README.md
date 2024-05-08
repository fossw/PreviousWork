
## Description
- get_unigene_information.py: Takes in two command line arguments (host name and gene name) 
and returns an index of which tissues that gene is expressed in for the provided host organism,
as well as a message with the number of gene occurrences. The organisms and
genes which can be used in this program are limited to those provided in the assignment5_data directory.


## Dependencies
- Must have Python installed


## Executing program
- $ python3 get_unigene_information.py --host host_name --gene gene_name
  - Example: $ python3 get_unigene_information.py --host "Homo sapiens" --gene AATK


## Authors
- Wyatt Foss


## Date Created
- 04/11/2024


## Tests for io_utils.py
- test_io_utils_for_reading: tests to see if a file can be read
- test_io_utils_for_writing: tests to see if a file can be written
- test_valueerror: tests if ValueError alarm properly functions
- test_oserror: tests if OSError alarm properly functions
