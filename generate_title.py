import json
import random
import os
from pathlib import Path

with open( os.path.join(Path(os.path.dirname(__file__)).absolute() , "markov_data.json") ,"r") as f:
    data = json.load(f)

markov_data = data["markov_data"]
starting_words = data["starting_words"]   

def generate_title():

    word = random.sample(starting_words,1)[0]
    rantitle = word
    no_words = 0
    while True:
        data = markov_data[word]
        
        total_weight = sum(data.values())
        if (total_weight < 3):
            data.update({ k:1 for k in random.sample(markov_data.keys(),3-total_weight) }) 

        newword = random.choices(list(data.keys()) , weights=list(data.values()), k=1)[0]
    
        if newword == "\n":
            if no_words < 3:
                continue
            else:
                break

        if (len(rantitle) + len(newword) + 1) > 280:
            break

        rantitle += " " + newword
        
        word = newword
        no_words += 1
    
    return rantitle

