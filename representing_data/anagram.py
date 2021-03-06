from wordsets import english_words_small
from _collections import defaultdict

def turn_a_word_into_a_list(word):
    letters = [char for char in word.lower()]
    return letters


def check_both_words_same_letters(word1, word2):
    cond1 = len(word1) == len(word2)
    cond2 = all(item in word1 for item in word2)
    return cond1 and cond2


def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """
    ## 1st Solution
    # does not work if "Adaaam" and "Adamm"
    # list_of_letters = turn_a_word_into_a_list(letters)
    # output_set = set()
    # for word in words:
    #     list_of_word_char = turn_a_word_into_a_list(word)
    #     if check_both_words_same_letters(list_of_letters, list_of_word_char):
    #         output_set.add(word)

    # 2nd solution
    # lookup = {}
    # for word in words:
    #     key_to_lookup = ''.join(sorted(word))
    #     if key_to_lookup not in lookup:
    #         lookup[key_to_lookup] = set()
    #     lookup[key_to_lookup].add(word)
    # check_this_word = ''.join(sorted(letters))
    # return lookup.get(check_this_word, set())

    # 3rd solution
    lookup = defaultdict(set)
    for word in words:
        lookup[''.join(sorted(word))].add(word)
    search = ''.join(sorted(letters))
    return lookup.get(search, set())


if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ").lower().strip()
        print(find_anagrams(letters, english_words_small))