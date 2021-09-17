from collections import Counter
import re


def count_unique_words(filename):
    # your code here
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
    pattern = re.compile("[^A-Za-z0-9]")
    content_splitted = pattern.split(content)
    words = [word.strip().lower() for word in content_splitted if word]
    count_word = Counter(words)
    for word, count in count_word.most_common(10):
        print(word, count)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')