# Three programs in Python:
  - get_gene_description.py
  - count_categorized_genes.py
  - find_intersections.py
  
## Description
- get_gene_description.py: This program takes a user provided gene name from
 a user-provided file and returns the description of the gene
- count_categorized_genes.py: This program counts how many genes are in each category based on the categories
 listed in the chr21_genes_categories.txt and prints the output in a separate file
- find_intersections.py: This program finds the intersection of gene names in two given files

## Dependencies
- Must have Python installed

## Executing program
- $ get_gene_description.py -i infile
  - Example: $ python3 get_gene_description.py -i chr21_genes.txt
- $ python3 count_categorized_genes.py -i1 infile1 -i2 infile2
  - Example: python3 count_categorized_genes.py -i1 chr21_genes.txt -i2 chr21_genes_categories.txt
- $ python3 find_intersections.py -i1 infile1 -i2 infile2
  - Example: python3 find_intersections.py i1 chr21_genes.txt -i2 HUGO_genes.txt

## Authors
- Wyatt Foss

## Date Created
- 03/18/2023

## Tests for io_utils.py
- test_io_utils_for_reading: tests to see if a file can be read
- test_io_utils_for_writing: tests to see if a file can be written
- test_valueerror: tests if ValueError alarm properly functions
- test_oserror: tests if OSError alarm properly functions