import random

def wordFetch(wordlist):
    word = random.choice(wordlist)

    return word

mylst = ["apple", 'banana', 'carriage', 'dog', 'earth', 'watermelon', 'pi', 'dinosaur', 'coconut', 'sunflower',
         'dawn', 'despair', 'lightning', 'northwest','cruise','mission','tarantula','fortress']

print(wordFetch(mylst))
