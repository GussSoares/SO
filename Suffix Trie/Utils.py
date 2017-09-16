#!/usr/bin/python3

import pprint


class SuffixTrie:

    def __init__(self):
        self.dictTrie = {}
        self.arrayGrams = []
        self.arrayAux = []
        self.level = 0

    def add_all(self, file):
        # file = open(file, "r")
        for n_gram in file:
            self.add(n_gram.rstrip())

    def add(self, n_gram):
        copy_n_gram = n_gram.split(" ")

        aux = self.dictTrie

        for word in copy_n_gram:
            if word not in aux:
                aux.update({word: {}})
                aux = aux[word]
            else:
                aux = aux[word]

    def contains(self, n_gram):
        copy_n_gram = n_gram.split(" ")

        aux = self.dictTrie

        for word in copy_n_gram:
            if word not in aux:
                return False
            else:
                aux = aux[word]

        return True

    def build_list_of_grams(self, trie):
        for key, value in trie.items():
            if len(key) != 0:
                self.arrayAux.append(key)
                self.build_list_of_grams(value)
                self.arrayAux.pop()
            else:
                self.arrayAux.append(key)
        self.arrayGrams.append(self.arrayAux.copy())

    def print_trie(self):
        p = pprint.PrettyPrinter(indent=4)
        p.pprint(self.dictTrie)


class SlidingWindow:
    def __init__(self, input, output):
        self.input_file = input
        self.number_lines = sum(1 for line in open(self.input_file))
        self.output_file = output

    def create_all_windows_between(self, begin, end):
        for number in range(begin, end + 1):
            self.create_sliding_window(number)

    def create_sliding_window(self, size_of_gram):
        begin = 0
        end = size_of_gram

        number_of_windows = self.number_lines - size_of_gram + 1

        i = 1
        while i <= number_of_windows:
            input_file = open(self.input_file, "r")
            output_file = open("window-" + self.output_file, "a")
            result = []
            for j, line in enumerate(input_file):
                if begin <= j < end:
                    result.append(line.rstrip())
            result = " ".join(result)
            output_file.write(result + "\n")
            input_file.close()
            output_file.close()
            i += 1
            begin += 1
            end += 1