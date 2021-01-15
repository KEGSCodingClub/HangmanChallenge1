#imports
from random import choice

#setup file in advance
with open('wordlist.txt','r') as f:
    wordList = f.read()
wordList = wordList.split('\n')

def searchWords(word):  #function to select words of a particular length
    if len(word) == length:
        return word


#option select
difficulty = input('What difficulty do you want to play on? Easy, medium, or hard?\n')

game = 'GO'
while game == 'GO':
    if difficulty.lower() == 'easy':    #create given list
        words = wordlist = ['apple', 'banana', 'carriage', 'dog', 'earth', 'watermelon', 'pi', 'dinosaur', 'coconut', 'sunflower', 'dawn', 'despair', 'lightning', 'northwest', 'cruise', 'mission', 'tarantula', 'fortress']

    elif difficulty.lower() == 'medium':    #transfer file
        words = wordList

    elif difficulty.lower() == 'hard':  #select specific lengths from file
        length = int(input('How long do you want your word to be? \t'))

        words = (map(searchWords,wordList)) #find words of correct length
        words = list(filter(None,words))    #get rid of wrong answers

        if len(words) == 0:
            print('No words of that length were found.\n')
            continue
    else:
        difficulty = input("That's not a difficulty - type easy, medium, or hard.")
        continue

    game = 'STOP'



print(choice(words).upper())    #output word