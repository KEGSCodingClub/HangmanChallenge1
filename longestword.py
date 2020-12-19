import json

with open("newlist.json","r") as f:
    data = json.load(f)
    a = 22
    for i in data:
        if len(data[i]) < a:
            a = len(data[i])
        #print(data[i])
print(a)