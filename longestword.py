import json

#checks for the shortest and longest word in the json file
# switching the signs and changing a to 22 allows for you to find the shortest word
with open("newlist.json","r") as f:
    data = json.load(f)
    a = 22
    for i in data:
        if len(data[i]) < a:
            a = len(data[i])
print(a)