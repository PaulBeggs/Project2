import random


def random_valid_word(wordfile: str, length: int) -> str:
    f = open(wordfile, "r")
    t = f.readlines()
    valid_words = []
    for w in t:
        stripped_word = w.strip()
        if len(stripped_word) == length:
            valid_words.append(stripped_word)
    while True:
        r = int(random.random() * len(valid_words))
        word = valid_words[r]
        if word:
            return word