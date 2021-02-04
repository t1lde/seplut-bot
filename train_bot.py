from itertools import tee
import random
import json

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

with open("titles.txt", "r") as f:
    titles = f.readlines()
titles = [x.strip() for x in titles]

markov_data = {}
starting_words =set() 

for title in titles:
    words = title.split(" ") 
    words.append("\n")
    starting_words.add(words[0])
    for a,b in pairwise(words):
        if a in markov_data:
            markov_data[a][b] = markov_data[a].get(b, 0) + 1
        else:
            markov_data[a] = {b:1}

with open("markov_data.json", "w") as f:
    json.dump({"markov_data": markov_data, "starting_words":list(starting_words)}, f)

