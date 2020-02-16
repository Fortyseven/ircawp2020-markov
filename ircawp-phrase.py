#!/bin/python3

import os
import sys
from Markov import *
import jsonpickle


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: {}  brain.json".format(sys.argv[0]))
        sys.exit(-1)

    if (not os.path.exists(sys.argv[1])):
        print("Brain not found '{}'".format(sys.argv[1]))
        sys.exit(-1)

    brainfile = open(sys.argv[1], "r")

    brain = jsonpickle.decode("".join(brainfile.readlines()))

    markov = Phrase(brain)
    print(markov.create())
