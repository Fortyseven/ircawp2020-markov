#!/bin/python3

import sys
import os
from Markov import *
import jsonpickle


if __name__ == "__main__":
    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("usage: {} sourcefile.txt [existingbrain.json]".format(
            sys.argv[0]))
        sys.exit(-1)

    if (not os.path.exists(sys.argv[1])):
        print("Can't find source corpus {}".format(sys.argv[1]))
        sys.exit(-1)

    existing_brain = None

    # If specified, load the existing brain and get it ready to merge
    if (len(sys.argv) == 3):
        if (not os.path.exists(sys.argv[2])):
            print("Can't find brain '{}' to merge with".format(sys.argv[2]))
            sys.exit(-1)

        existing_brain_f = open(sys.argv[2], "r")
        existing_brain = jsonpickle.decode(
            "".join(existing_brain_f.readlines()))

    brain = MarkovBuildBrain(sys.argv[1], existing_brain)
    print(jsonpickle.encode(brain))
