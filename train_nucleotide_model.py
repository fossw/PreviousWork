#!/usr/bin/env python
# train_nucleotide_model.py

"""This program takes in two fasta files and trains two models to represent the transition probabilities between nucleotides for sequences in each"""

import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

baseIDx = {"A": 0, "C": 1, "G": 2, "T": 3}


def main():
    spaciiFA = "MSpacii.fa"
    pathogenFA = "pathogen.fa"
    spaciiFA_T = "MSpacii_training.fa"
    pathogenFA_T = "pathogen_training.fa"
    spaciiID2seq = getSeq(spaciiFA)
    pathogenID2seq = getSeq(pathogenFA)

    spaciiTrainModel = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    pathTrainModel = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    spaciiTrainModel = trainModel(spaciiTrainModel, spaciiFA_T)
    pathTrainModel = trainModel(pathTrainModel, pathogenFA_T)

    markovScoresSpacii = []
    markovScoresPath = []

    for ID in spaciiID2seq.keys():
        markovScoresSpacii.append(getLogLike(spaciiTrainModel, pathTrainModel, spaciiID2seq[ID]))
    for ID in pathogenID2seq.keys():
        markovScoresPath.append(getLogLike(spaciiTrainModel, pathTrainModel, pathogenID2seq[ID]))

    ####----------------------output-------------------------
    plt.hist([markovScoresPath, markovScoresSpacii], bins=20, label=['pathogen', 'spacii'], rwidth=1, density=True,
             color=['red', 'blue'])
    plt.show()
    scoresOutputText(markovScoresSpacii, markovScoresPath)
    ####----------------------output-------------------------


def scoresOutputText(markovScoresSpacii, markovScoresPath):
    f = open("results.tab", "w")
    f.write("SpaciiScores\tpathogenScores\n")
    for i in range(len(markovScoresSpacii)):
        f.write(str(markovScoresSpacii[i]) + "\t" + str(markovScoresPath[i]) + "\n")
    f.close()


def getLogLike(model1, model2, seq):  # takes in the two trained models and the sequence that needs to be scored
    """returns the log-likelihood of the two models"""

    Pmod1 = 1
    Pmod2 = 1

    for IDx in range(1, len(seq)):
        x1 = baseIDx[seq[IDx]]
        x1min1 = baseIDx[seq[IDx-1]]
        Pmod1 += math.log(model1[x1][x1min1]) # compute log probability of first model
        Pmod2 += math.log(model2[x1][x1min1]) # compute log probability of second model

    score = Pmod1 - Pmod2
    return score


def trainModel(model, data):
    """This function calculates how many dinucleotides preceed each base.
    Returns a 4x4 matrix, each row representing the probability of seeing base x given previous base y"""

    seqstring = getSeq(data)
    x1min1 = -1
    for seq in seqstring.values():
        for base in seq:
            x1 = baseIDx[base]
            if x1min1 >= 0:
                model[x1min1][x1] += 1
            x1min1 = x1

    for nuc in [0, 1, 2, 3]:
        trans_sum = sum(model[nuc])
        for dinuc in [0, 1, 2, 3]:
            model[nuc][dinuc] = round(model[nuc][dinuc] / trans_sum, 3)

    print(model)
    return model


def getSeq(filename):
    "Parses lines in a fasta file and returns a dictionary of sequences"

    f = open(filename)
    id2seq = {}
    currkey = ""
    for line in f:
        if line.find(">") == 0:
            currkey = line.rstrip()[1:]
            id2seq[currkey] = ""
        else:
            id2seq[currkey] = id2seq[currkey] + line.rstrip()
    return id2seq


main()

