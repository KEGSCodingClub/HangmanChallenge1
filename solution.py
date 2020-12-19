import random as r
import json
import time as t
import string

with open('newlist.json') as f:
    data = json.load(f)


length = int(input("enter character length: "))
while length > 22 or length < 2:
    print("no words with given value, please try again")
    length = int(input("enter character length: "))

choice = ""
completed = 0
while choice == "":
    rand = r.randint(0,58108)
    if len(data[json.dumps(rand)]) == length:
        choice = data[json.dumps(rand)]
        break
choice = choice.upper()

chosen = []
current = "_ " * length
triesleft = 5
while completed < length and triesleft > 0:
    print("\n\n")
    print("YOU HAVE",triesleft,"GOES REMAINING")
    print("CHOOSE A LETTER!\n\n\n")
    t.sleep(1)
    print(current)
    letter = input("-> ")
    while len(letter) > 1 or letter not in list(string.ascii_letters):
        print("your string is not a letter or too long!")
        letter = input("\n-> ")
    letter = letter.upper()
    
    if letter in chosen:
        print("ALREADY CHOSEN!")
        continue
    if letter in list(choice):
        chosen.append(letter)
        print("CORRECT!")
        for i,x in enumerate(choice):
            if x == letter:
                current = current[:(i*2)] + letter + current[(i*2)+1:]
                completed += 1
    else:
        chosen.append(letter)
        triesleft -= 1
        print("OH DEAR! THE LETTER ISN'T HERE!")

if triesleft == 0:
    print("\n\n\n YOU LOSE!")
else:
    print("\n\n\n YOU WIN!")