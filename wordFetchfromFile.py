import random

def wordFetch():
    with open("wordlist.txt") as word_file:
        words = word_file.read().split()
        word = random.choice(words)
        return word

print(wordFetch())