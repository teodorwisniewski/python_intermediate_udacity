import helper
import gold
from collections import  defaultdict
import string
import itertools


def parse_content(content):
    """
    input: 'the 6801236995\nof  4099953905\nand 2849894962\nto  2404880449\nin  2060698546\na   1816123747\nis
    1016808911\nthat
    output: {'the': 6801236995,
             'of': 4099953905,
             'and': 2849894962,
             'to': 2404880449,
             'in': 2060698546,
             'a': 1816123747,
             'is': 1016808911,
             'that': 988064813,
             'it': 767931969,
             'for': 742223348,
             'was': 730667902,
             'as': 714194445
             }
    output:
    :param content:
    :return:
    """
    splitted_words = content.split("\n")
    output = {
        word.split()[0]: int(word.split()[1])
        for word in splitted_words
    }
    return output

def make_tree(words):
    """
    output: {'t': {'h': {'e': {'$the': 6801236995,
    'y': {'$they': 326802098},
    'i': {'r': {'$their': 293103846, 's': {'$theirs': 1292925}}},
    'r': {'e': {'$there': 205528704,
      'f': {'o': {'r': {'e': {'$therefore': 37414333}}}},
      'b': {'y': {'$thereby': 4273102}},
      'o': {'f': {'$thereof': 4183101}, 'n': {'$thereon': 958176}},
      'i': {'n': {'$therein': 2356664}},
      'a': {'f': {'t': {'e': {'r': {'$thereafter': 1621058}}}}},
      't': {'o': {'$thereto': 1080240}},
      'u': {'p': {'o': {'n': {'$thereupon': 1066065}}}}},
    :param words:
    :return:
    """
    trie = {}
    for word, freq in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[f"${word}"] = freq
    return trie


def get_leaves_from_trie(d, result=None):
    output_leaves = []
    for key, value in d.items():
        if isinstance(value,dict):
            output_leaves = get_leaves_from_trie(value, result=output_leaves)
        else:
            output_leaves.append((key[1:], value))
    return output_leaves


def predict(tree, numbers):
    """
    output: [('opinion', 16087460),
     ('original', 14099787),
     ('organization', 10092822),
     ('origin', 8307819),
     ('opinions', 4940942),
     ('organized', 4936097),
     ('originally', 4334305),
     ('organizations', 3800715)]
    :param tree:
    :param numbers:
    :return:
    """
    letters_a_to_z = string.ascii_lowercase
    # dictionary containing mappings between numbers and letters
    # on the cell phone keyboard
    t2_mapping = {}
    numbers_2_to9  = list(range(2,10))
    for i, number in enumerate(numbers_2_to9):
        t2_mapping[number] = letters_a_to_z[i*3:3*(1+i)]
    t2_mapping[numbers_2_to9[-1]] = t2_mapping[numbers_2_to9[-1]] + letters_a_to_z[-1]
    possible_letters_subsets = []
    for number in numbers:
        number = int(number)
        possible_letters_subsets.append(t2_mapping[number])
    combs = list(itertools.product(*possible_letters_subsets))

    output_words = []
    for comb in combs:
        inner_trie = tree
        for ch in comb:
            inner_trie = inner_trie.get(ch, None)
            if inner_trie is None:
                break
        if inner_trie is not None:
            new_words = get_leaves_from_trie(inner_trie)
            output_words.extend(new_words)

    return output_words


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break

