#!/usr/bin/python3

from Utils import SuffixTrie
from Utils import SlidingWindow


def main():
    string_of_prefixes = ["a b", "a b a", "a b c", "a d", "b a", "b a d", "b a g"]

    kilvia = { "identificacao": { "nome": "Kilvia", "sobrenome": "leticia", "idade": 19 }, "endereco": { ... } }

    trie = SuffixTrie()

    # window = SlidingWindow("ls-without-id.txt", "result.txt")
    # window.create_all_windows_between(1, 3)

    # trie.add_all("window-result.txt")
    trie.add_all(string_of_prefixes)
    trie.print_trie()

    trie.build_list_of_grams(trie.dictTrie)

    print("\n Data len: {0} \n\t {1}".format(len(trie.arrayGrams), trie.arrayGrams))


if __name__ == '__main__':
    main()

