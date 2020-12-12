# REQUIRES PYTHON 3.8 OR ABOVE FOR THE HARD FUNCTION TO WORK

import random


def easy():
    wordlist = ['apple', 'banana', 'carriage', 'dog', 'earth', 'watermelon', 'pi', 'dinosaur', 'coconut', 'sunflower', 'dawn', 'despair', 'lightning', 'northwest', 'cruise', 'mission', 'tarantula', 'fortress']
    return wordlist[random.randint(0, len(wordlist)-1)]


def medium():
    with open("wordlist.txt", "r") as f:
        wordlist = f.readlines()
    return wordlist[random.randint(0, len(wordlist)-1)].strip()


def hard():
    with open("wordlist.txt") as f: return f"Found word: {(filteredwordlist := list(filter(lambda a: len(a) == inp, wordlist)))[random.randint(0, len(filteredwordlist)-1)]} from {len(filteredwordlist)} possible words.\n" if 1 < (inp := int(input("Enter the length of the word you want\n>>>\t"))) <= max(map(lambda a: len(a), (wordlist := f.read().splitlines(False)))) else f"Invalid length. Max length is: {max(map(lambda a: len(a), wordlist))}"
    # Had to repeat the code for max length to fit it on one line and also tell you what the max length is.
    # Shouldn't impact performance unless wordlist very large.


print(easy())
print(medium())
while True:
    print(hard())
