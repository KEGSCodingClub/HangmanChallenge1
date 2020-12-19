import random as r
import json

with open('newlist.json') as f:
    data = json.load(f)

print(data["hello"])
length = int(input("enter character length: "))
choice = ""
while choice == "":
    rand = r.randint(0,370101)
    print(choice[rand])