import helper
import gold
from collections import  defaultdict

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


def predict(tree, numbers):
    return {}


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

