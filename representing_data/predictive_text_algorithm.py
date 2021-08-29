import helper
import gold
from collections import  defaultdict
import string
from itertools import product, combinations, chain


def parse_content(content):
    splitted_content = content.split('\n')
    outdict = {}
    for el in sorted(splitted_content):
        word, frequency = el.split()
        outdict[word] = int(frequency)
    return outdict


def make_tree(words):
    trie = {}
    for word, freq in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            # passing reference to the most inner node/dict in the tree for a given word
            node = node[ch]
        # last node for all characters get a word
        node[f"${word}"] = freq

    return trie


def get_values(d, result=None):
    if result is None:
        result = []
    for key, value in d.items():
        if isinstance(value,dict):
            get_values(value, result=result)
        if "$" in key:
            result.append((key[1:],value))
    return result

def predict(tree, numbers):
    letters_az = string.ascii_lowercase
    numbers_t9 = '23456789'
    mapping_numbers_to_letters_t9 = {}
    for i, number in enumerate(numbers_t9):
        letters = letters_az[i*3:3*(1+i)]
        mapping_numbers_to_letters_t9[number] = letters
    mapping_numbers_to_letters_t9[number] = mapping_numbers_to_letters_t9[number] + letters_az[-1]
    numbers_to_letters = {}
    for i, number in enumerate(numbers):
        letters = mapping_numbers_to_letters_t9[number]
        numbers_to_letters[f"i={i+1}={number}"] = [ch for ch in letters]
    combs = list(product(*numbers_to_letters.values()))
    results = []
    for comb in combs:
        node = tree
        for ch in comb:
            node = node.get(ch,None)
            if node is None:
                break
        if node is not None:
            new_word = get_values(node)
            results.extend(new_word)

    return results


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

