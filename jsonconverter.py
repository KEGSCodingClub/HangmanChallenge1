import json

a = ""
with open("wordlist.txt") as f:
    with open("newlist.json","w") as t:
        t.write("{")
        for i,x in enumerate(f):
            t.write("\""+str(i)+"\""+":"+"\""+str(x).strip()+"\""+",")
        t.write("}")
