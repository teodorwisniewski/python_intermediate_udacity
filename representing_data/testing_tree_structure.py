

def make_tree(words):
    trie = {}
    for word, frequency in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[f'${word}'] = frequency

    return trie

if __name__ == "__main__":
    words = {"siemano":534545, "siema":324}
    make_tree(words)