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


```python3
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
```
__That's a lot of code!__ Don't worry, lets look through it ourselves.

```python3
    print("\n\n")
    print("YOU HAVE",triesleft,"GOES REMAINING")
    print("CHOOSE A LETTER!\n\n\n")
    t.sleep(1)
    print(current)
```
Firstly, we print our current *"status"*, which includes our number of remaining goes, a prompt for us to pick a letter, and the variable *current*,
which, if you may be able to recall, stores the outputted underscores and letters, showing us how many gaps we have left. We have quite a few ```\n``` statements
in our code, which is an escape character for creating a new line. It is simply there to make the console output look as if its *refreshing*. There are other ways
of clearing and reprinting the console, like in a real screen, but it is usually OS specific and furthermore, *console-specific*, making it unrealistic and quite 
messy to include it everywhere.

```python3
    letter = input("-> ")
    
    while len(letter) > 1 or letter not in list(string.ascii_letters):
        print("your string is not a letter or too long!")
        letter = input("\n-> ")
    letter = letter.upper()
```
This next section acts as validification to the inputted letter by the user. The first check involves whether it is a single character, hence the __>1__ statement.
The next check looks at whether the letter is not in the list of characters in the alphabet. ```string.ascii_letters``` is a *constant array* containing all the
__lowercase and uppercase__ letters in the english alphabet, hence representing our field of input (our *keyboard* per-se). Once we have our desired input, we convert the letter into uppercase, in-case the input provided was in lowercase, since earlier we converted our choice entirely into uppercase.

```python3
    if letter in chosen:
        print("ALREADY CHOSEN!")
        continue
```
if our chosen letter is already in the *chosen* list from earlier, then we can return to the user that the selected letter is already chosen. This acts as further __validification__. You may have seen me use this ```continue``` keyword quite often in my code; it is simply a *control-statement* that allows for the code to directly skip to its next cycle mid-loop, essentially skipping all the code below it. 

```python3
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
```
Here is the main logic behind the hangman game. If our desired letter, being fully checked, is in the *choice string*, being temporarily converted into a list, we can
then append it to the *chosen list* and notify the user that they have successfully picked the right letter. Here comes the tricky part: we need a way of showing to the user updated version of the variable *current* with all the parts where the correct letter applies. 
if the word was __"APPLE"__, and the user's first guess was __"P"__, then we would want to change from ```_ _ _ _ _ ``` to ```_ P P _ _```

- Firstly, we enumerate through the choice string. ```enumerate(iterable-type)``` is a very handy function when doing a __for loop__. It is a custom version of __range()__ which returns a tuple of both the index and the item itself. It is, essentially, a mix of ```for i in list``` and ```for i in range(len(list))```
- In the loop, we check whether the letter at the current loop index is in-fact the correct letter. If so, we perform a splice where we insert *x* into the current string. ```current[:(i*2)]``` depicts the entire string up to the underscore where the letter should be, exclusive of the underscore, and ```current[(i*2)+1:]``` depicts the entire string from the end down to the underscore where the letter should be, exclusive of the underscore because of the +1. We then fit our letter between the two splices and make the result the new *current* variable.

If our letter __iss not__ correct, not being in the choice string, then we append the letter to the *chosen list* and substract from the number of goes left. We notify the user that he has made an incorrect letter choice.


```python3
if triesleft == 0:
    print("\n\n\n YOU LOSE!")
else:
    print("\n\n\n YOU WIN!")
```
__This is the very last part of the code!__
We reach this part of the code *after the while loop is finished*, which, if we look back at the conditions for the loop, could be because of 2 reasons:
- The user has successfully picked all the letters in the word
- The user has run out of goes.
Therefore, we check the value of *triesleft* and we can deduce that if it is a number above 0, then the user must have won by guessing the words correctly.
__That's all!__



## Json Converter program 

[This is the program I used to convert wordlist.txt into newlist.json](https://github.com/KEGSCodingClub/HangmanChallenge1/blob/RudrrayanManna/jsonconverter.py)
```python3
import json

a = ""
with open("wordlist.txt") as f:
    with open("newlist.json","w") as t:
        t.write("{")
        for i,x in enumerate(f):
            t.write("\""+str(i)+"\""+":"+"\""+str(x).strip()+"\""+",")
        t.write("}")

```
The code here is quite obfuscated, in an attempt to make it shorter. We firstly open the *wordlist.txt* file, as variable f, and then create a new file, *newlist.json* as t, and mark it as "w", meaning that we can only write to this file. We firstly write a *"{"* to the file, being the opening bracket of the json file, and proceed to enumerate through the contents of *f*. The following write encompasses the *key-value pair* for each of the json elements:
- we firstly write the key as a number, being *i* in f, we must include double-quotes since it is the type that JSON uses. __Remember to use a backslash!__
- we then add a colon as a *key-value separator* and add the actual word as *x* in f, within doube-quotes. It is important to use ```.strip()``` since it removes any unwanted whitespace from ruining the formatting for the JSON.
- Lastly, we add a *","* as a separater for each *key-value pair*. 

We can then use an [online JSON beautifier](https://jsonformatter.curiousconcept.com) to make the json *look nice*. This is purely optional, and only for the sake of my sanity when trying to debug something. Also, if you are going to try out the code for yourself, be sure to go to the end of the json and remove the comma at the end!

We end the program with a final *"}"* to close the JSON field.


## word length program

This is a very small utility program for finding the smallest and largest word in the json file

```python3
import json

with open("newlist.json","r") as f:
    data = json.load(f)
    a = 0
    for i in data:
        if len(data[i]) > a:
            a = len(data[i])
```
As you can see, the code isn't __too bad__ for this program. Like before, we open a json file, this time marked as "r" for __read-only__. We then create a variable, *data*, which has the loaded json string from the file. We then loop through *data*, and update *a*, which is currently initialised as 0, and only update it if the the element in the loop is greater than what a currently is. By the end of it, *a* should be equal to *the __longest word__ in the json file*
If we want to find the shortest word in the json file, we take the result of the largest word, and we initialise *a* as that. we then simply swap the signs and *a* should, at the end, be equal to the length of the *shortest word*.
Here is the code for that:
```python3
import json

with open("newlist.json","r") as f:
    data = json.load(f)
    a = 22
    for i in data:
        if len(data[i]) < a:
            a = len(data[i])
```
