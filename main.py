#imports
from random import choice

#setup file in advance
with open('wordlist.txt','r') as f:
    wordList = f.read()
wordList = wordList.split('\n')


def searchWords(word):
    if len(word) == length:
        return word

length = int(input('How long do you want your word to be? \t'))

words = (map(searchWords,wordList)) #find words of correct length
words = list(filter(None,words))    #get rid of wrong answers

print(choice(words).upper())    #output word