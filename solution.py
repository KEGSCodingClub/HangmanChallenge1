import random as r
import json
import time as t
import string

#loads the json file of all the words
with open('newlist.json') as f:
    data = json.load(f)


# input length of character. used "longestword.py" to create the constraints
length = int(input("enter character length: "))
while length > 22 or length < 2:
    print("no words with given value, please try again")
    length = int(input("enter character length: "))

#initialise some variables.
choice = ""
completed = 0

#randomly looks through the json with Θ(1) worst case scenario would be O(n). A most terrible scenario would be infinite since
#I am not storing previously looked up elements and because it is random-based.
while choice == "":
    rand = r.randint(0,58108)
    if len(data[json.dumps(rand)]) == length:
        choice = data[json.dumps(rand)]
        break
#make all the letter types the same
choice = choice.upper()

#record of chosen letters
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
    
    #validifies the letter input
    while len(letter) > 1 or letter not in list(string.ascii_letters):
        print("your string is not a letter or too long!")
        letter = input("\n-> ")
    letter = letter.upper()
    
    #checks if the letter has already been chosen
    if letter in chosen:
        print("ALREADY CHOSEN!")
        continue
    
    #if the letter is in the word, change current (the print output for the underscores) with all occurences of the correct letter
    #and add to chosen
    #if the letter is incorrect, substract from the total goes left and add to chosen.
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

#end statement
if triesleft == 0:
    print("\n\n\n YOU LOSE!")
else:
    print("\n\n\n YOU WIN!")