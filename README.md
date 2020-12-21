# SOLUTION DESCRIPTION
> this is my solution to the *hard* section of the Hangman Challenge

I have 2 utility files: 
- [jsonconverter.py](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/jsonconverter.py): for converting wordlist.txt into newlist.json
- [longestword.py](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/longestword.py): for finding the shortest and longest word in a json file

### Why did I convert to json?
- I attempted to load the file by simple reading the text line by line, which is how python supports it, but found it to be extremely slow.
- The reason for this was because the lookup time for anything in wordlist.txt is O(N), which is incredibly slow for 58,109 words.
- It will be even worse later down the line when finding words of certain lengths randomly
- Furthermore, I have heard that some people are using some *shuffling techniques* to find a word of specific length to avoid having to label each word, which would be slow. However, even then, the best shuffling algorithm out there __The Fisher Yates__ Random permutation algorithm, only operates in O(N) 
assuming that the lookup time is O(1), making the total complexity O(N^2) when not using a hash table or JSON, which is undeniably slow.

> Therefore, I decided to use the JSON format since it is completely serialized and acts as a hashmap, with a constant lookup time of O(1) (most of the time)
> which allowed for choosing a random length word to be reduced to a worst case of N, much better than having to sort or label each of the words
> A disadvantage of this is that, it is possible for the program to go on forever, although with an extremely, infinetessimaly small probability, since finding a random
> word of a fixed length would use a random number generator. There is no upper bound theoretically, similar to bogosort, but the chances are very small.

## Initialisation and getting the choice

```python3
import random as r
import json
import time as t
import string
```
*Here I am importing time to allow for some breaks in the program, purely for the user*

Here are all of the initial imports that I will be using. The __JSON__ import allows for us to access the
[*Newlist.json*](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/newlist.json) file. 
> See more on the JSON conversion process [here](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/README.md#json-converter-program)

The __random__ import allows us to pick a word of a fixed length and the __string__ import gives us a selection of ascii to create letter constraints.

```python3
with open('newlist.json') as f:
    data = json.load(f)

length = int(input("enter character length: "))
while length > 22 or length < 2:
    print("no words with given value, please try again")
    length = int(input("enter character length: "))
```
The first two lines initialised the *data* variable containing the opened [*Newlist.json*](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/newlist.json) file. 
Apparantly the new convention is to use:
```python3
with open('x.filetype') as variable:
```
However it is completely feasible to use this:
```python3
data = json.load(open('x.filetype'))
```
The next section of code involves taking the User input for the character length via variable *length*. Make sure to wrap the input with __int()__.
A __while loop__ covers the *validation process* for the user input. if the value provided by the user is greater than 22 or less than 2, we can say
that there are no words of the given size. To avoid the code becoming slightly too *obfuscated* I have excluded mistyped letters in the input field or 
checking whether the user has given the worded version of a number such as __one__ instead of __1__. To see how I found the constraints of the word length
please check my explanation on [the longest shortest word program](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/README.md#word-length-program).
 

```python3
choice = ""

while choice == "":
    rand = r.randint(0,58108)
    if len(data[json.dumps(rand)]) == length:
        choice = data[json.dumps(rand)]
        break

choice = choice.upper()
```
This last segment of code prior to the actual game involves the *choice selection*. The variable *choice* is first initialised and a __while loop__ goes 
through to find randomly selected word of our length. The process involves picking a random number between 0 and 58,108 and storing it in *rand*. We will
then check if the __key__ at this randomly generated number has a value of our desired length. If this is not the case then we continue. Once we find our
random word we can *break out of the loop*. An "average-worst" case scenario for this code would be around Θ(N) since the lookup time is O(1) and we will 
be going through random words. However, since we are not recording our *previously visited* words in a list for the sake of auxilary space, we could quite
possibly end up with a "terrible" case scenario of __O(N!)__, which could happen if there was only one word of the desired length. Although I have not included
the visited word list in my own code, ~~since I was slightly lazy~~, we can see how this can be implemented right now:

```python3
choice = ""
choicelist = [d for d in range(58109)]

while choice == "":
    rand = r.choice(choicelist)
    if len(data[json.dumps(rand)]) == length:
        choice = data[json.dumps(rand)]
        break
    choicelist.pop(rand)

choice = choice.upper()
```
__Now this solution removes the N! and infinity scenario. Hooray!__
Assuming that the choice() function has a time complexity of O(1) (which is possible), we can say that this new algorithm has a worst case scenario of __O(N)__
where *N* is the original size of the array, and a best case scenario of __O(1)__!

The last line ```choice.upper()``` simply makes our choice fully uppercase to make letter choosing much easier. *now lets move onto the game itself:*


## The Hangman Process

We will now be moving onto the main game loop for the hangman challenge, lets start with some *initialisation*.
```python3
chosen = []
completed = 0
current = "_ " * length
triesleft = 5
```
Here, __chosen__ will be a store of all the letters we have chosen during the game, it will be initially empty.
The __completed__ variable is an integer which will store the amount of letters in the word we have guessed. Note that this is based on the total amount of letters
in the word and not our successfully chosen words, meaning that if the same letter occurs multiple times in the word, and we have chosen it, completed will go up by
x number of times. *The gameloop will break when it reaches the length of the word.*
The __Current__ variable is important for console output in the game. It is initially going to be some underscores for the total length of the word, but over time, 
we will see some of the underscores to be replaced by letters.
Lastly, the __triesleft__ variable simply stores our remaining goes, it is currently set to 5 and *the gameloop will break if it reaches 0*

## Json Converter program 

## word length program


