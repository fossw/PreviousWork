#!/usr/bin/env python
# identifyORFs.py

from Bio import SeqIO
import re

"""This program takes an input file with assembled contigs,
identifies the most likely ORFs from a set of contigs, 
and writes the ORFs with their respective lengths and positions to a FASTA file"""

motif = [[.5, .5, .5, .5, 0, 0, 0, 0, 0, 2, -99, -99, .5],  # A
         [0, 0, 0, 0, 0, 0, 0, 0, 0, -99, 2, -99, 0],  # T
         [0, 0, 0, 0, 0, 0, 0, 0, 0, -99, -99, -99, 0],  # C
         [.5, .5, .5, .5, 0, 0, 0, 0, 0, .5, -99, 2, 0]]  # G

def scanSeq(seq):
    """searches a single sequence for possible orfs. Returns
    start positions, lengths and sequences of ORFs"""
    potentialStartPositions = []
    ORFSeqs = []
    ORFlengths = []
    k = 13

    end = len(seq) - k + 1
    for position in range(0, end):
        kmer = seq[position:position + k]
        motifscore = scoreMotif(kmer)
        startpos = position + 9
        # Only chose motifs which align best with the motif
        if motifscore > 7.25:
            startseq = seq[startpos:]
            for stopcodon in re.finditer('TAA|TAG|TGA', startseq):
                # search for start and stop codon
                orf = startseq[:stopcodon.end()]
                # ORF must be divisible by 3 to be coding
                if len(orf) % 3 == 0:
                    # Filter out short ORFs
                    if len(orf) >= 60:
                        potentialStartPositions.append(startpos + 1)
                        ORFSeqs.append(orf)
                        orflen = len(orf)
                        ORFlengths.append(orflen)
                        break


    return potentialStartPositions, ORFSeqs, ORFlengths

def scoreMotif(unscored):
    """scores a sequence the same length as the motif[13
    bases]. Returns motif score."""
    seq = unscored
    seqscore = []
    # find the positions and score of each nucleotide in the 13-mer
    for position in range(len(seq)):
        if seq[position:].startswith('A'):
            seqscore.append(motif[0][position])
        if seq[position:].startswith('T'):
            seqscore.append(motif[1][position])
        if seq[position:].startswith('C'):
            seqscore.append(motif[2][position])
        if seq[position:].startswith('G'):
            seqscore.append(motif[3][position])
    # Total motif score is the sum of scores for nucleotides in their respective positions
    motifscore = sum(seqscore)
    return motifscore

def identifyORFs():
    """searches a single sequence for possible orfs. Returns
    start positions, lengths and sequences of ORFs"""

    outfile = open("true_orfs.fa", "w")  # write new file for ORF output
    contig_count = 0

    for record in SeqIO.parse("spaceSeq.fa", "fasta"):
        contig_count += 1
        # Use scanSeq function to find every true ORF from the input sequences
        potentialStartPositions, ORFSeqs, ORFlengths = scanSeq(str(record.seq))
        pos = str(potentialStartPositions)[1:-1]
        orf = str(ORFSeqs)[1:-1]
        orf = orf.replace("'", "")
        length = str(ORFlengths)[1:-1]
        # write ORFs to output file in FASTA format
        if len(list(ORFSeqs)) == 1:
            outfile.write(f">contig {contig_count}|Length {length}|at position {pos}\n{orf}\n")
        # if there is more than one ORF in a contig, write as a separate FASTA entry
        if len(list(ORFSeqs)) > 1:
            outfile.write(f">contig {contig_count}|Length {list(ORFlengths)[0]}|at position"
                          f" {potentialStartPositions[0]}\n{list(ORFSeqs)[0]}\n")
            outfile.write(f">contig {contig_count}|Length {list(ORFlengths)[1]}|at position"
                          f" {potentialStartPositions[1]}\n{list(ORFSeqs)[1]}\n")


identifyORFs()

