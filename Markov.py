from random import randrange
import jsonpickle

#################################################################


class Root():
    def __init__(self):
        self.words = {}

#################################################################


class Node():
    def __init__(self, start_word=False, end_word=False):
        self.start = start_word
        self.end = end_word
        self.next = {}

#################################################################


class Phrase():
    def __init__(self, brain):
        self.brain = brain

    def generatePhrase(self):
        self.phrase = []
        candidates = []
        for word in self.brain.words:
            if self.brain.words[word].start:
                candidates.append(word)

        cur_word = candidates[randrange(len(candidates))]
        self.phrase.append(cur_word)

        finished = False
        while not finished:
            next_candidates = []

            for word in self.brain.words:
                if (word in self.brain.words[cur_word].next.keys()):
                    count = self.brain.words[cur_word].next[word]
                    for i in range(count):
                        next_candidates.append(word)

            next_word = next_candidates[randrange(len(next_candidates))]

            self.phrase.append(next_word)

            cur_word = next_word

            if (self.brain.words[cur_word].end):
                finished = True

            if (cur_word[-1] in ['.', '?', '!']):
                if randrange(1) == 0:
                    finished = True

    def create(self):
        self.generatePhrase()
        sentence = ' '.join(self.phrase)
        if (sentence.count('"') == 1):
            sentence = sentence.replace('"', '')

        return sentence

#################################################################


class Brain():
    def __init__(self, existing_brain=None):
        if (existing_brain):
            self.brain = brain
        else:
            self.brain = Root()

    def loadExistingBrain(self, brain_path):
        f = open(brain_path, "r")
        self.brain = jsonpickle.decode("".join(f.readlines()))

    def compileCorupus(self, source_text):
        file = open(source_text, "r")
        corpus = file.readlines()
        for line in corpus:
            self.processLine(line)

    def processLine(self, line):
        line_pieces = line.split(' ')
        is_start = True
        is_end = False

        while len(line_pieces):
            line_pieces[0] = line_pieces[0].strip()

            if len(line_pieces) == 1:
                is_end = True
            else:
                line_pieces[1] = line_pieces[1].strip()

            if line_pieces[0] not in self.brain.words:
                self.brain.words[line_pieces[0]] = Node(is_start, is_end)

            is_start = False

            if not is_end:
                if line_pieces[1] not in self.brain.words[line_pieces[0]].next:
                    self.brain.words[line_pieces[0]
                                     ].next[line_pieces[1]] = 1
                else:
                    self.brain.words[line_pieces[0]
                                     ].next[line_pieces[1]] += 1

            line_pieces.pop(0)

    def toJSON(self):
        return jsonpickle.encode(self.brain)
