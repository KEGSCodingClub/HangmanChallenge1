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
 

## Json Converter program 

## word length program


