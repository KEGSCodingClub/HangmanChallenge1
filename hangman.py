##import random
##words= ["justice" , "probono" , "courtcase" , "diligence" , "audit" , "evasion"]
##
##word = words[random.randint(0,5)]
##display = ""
##for z in range(len(word)):
##    display += "*"
##print(word)
##print(display)

def wordFetch():
    return "scrumptious"
display = ""

word = wordFetch()

for z in range(len(word)):
    display += "*"

while display != word:
    guess = input("Enter a letter: ")
    for i in range(len(word)):
        if word[i] == guess: 
            display = display[:i] + guess + display[i+1:]
            print("Well done, you guessed a letter!")
            print(display)

    if guess not in word:
        print("This letter is not in the word, try again")

print("Congratulations, you have guessed the word: " + word)
