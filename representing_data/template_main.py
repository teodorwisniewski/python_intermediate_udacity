import helper
import gold
from collections import  defaultdict
import string
from itertools import product, combinations, chain


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
    pass

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
    pass

def get_values(d, result=None):
    pass

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
    pass


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = gold.parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = gold.make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = gold.predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break

