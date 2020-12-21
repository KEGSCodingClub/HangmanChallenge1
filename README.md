# SOLUTION DESCRIPTION
> this is my solution to the *hard* section of the Hangman Challenge

I have 2 utility files: 
- jsonconverter.py: for converting wordlist.txt into newlist.json
- longestword.py: for finding the shortest and longest word in a json file

### Why did I convert to json?
- I attempted to load the file by simple reading the text line by line, which is how python supports it, but found it to be extremely slow.
- The reason for this was because the lookup time for anything in wordlist.txt is O(N), which is incredibly slow for 58,109 words.
- It will be even worse later down the line when finding words of certain lengths randomly
> Therefore, I decided to use the JSON format since it is completely serialized and acts as a hashmap, with a constant lookup time of O(1) (most of the time)
> which allowed for choosing a random length word to be reduced to a worst case of N, much better than having to sort or label each of the words
> A disadvantage of this is that, it is possible for the program to go on forever, although with an extremely, infinetessimaly small probability, since finding a random
> word of a fixed length would use a random number generator. There is no upper bound theoretically, similar to bogosort, but the chances are very small.

## Program description

```python3
import random as r
import json
import time as t
import string
```
*Here I am importing time to allow for some breaks in the program, purely for the user*

Here are all of the initial imports that I will be using. The __JSON__ import allows for us to access the
[*Newlist.txt*](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/newlist.json) - 


