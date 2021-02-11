import random


with open("wordlist.txt") as file:
    file_words = file.read()
    wordlist = file_words.split()


def get_random(words):
    random_word = random.choice(words)
    return random_word


def check(w):
    length = input("Length of word (min = 2, max = 22): ")
    while len(w) != int(length):
        w = get_random(wordlist)
    else:
        print(w)


word = get_random(wordlist)
check(word)
