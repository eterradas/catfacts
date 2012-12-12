from random import choice,shuffle
from os import path

intro = ['Welcome to CatFacts! The coolest Way to learn about cats! Your first CatFact: Cats spend a third of their waking hours grooming themselves!'] 
signoff = [' Luv, CatFacts!', ' Awesome!', ' TO STOP REPLY <STOP>', 
           ' This is Catsfacts!', ' Meow!']

def generate_cat_facts_message_sequence():
    cat_facts_message_sequence =[]
    with open(path.join(path.dirname(__file__), "catfacts.txt")) as file:
        for line in file:
            cat_facts_message_sequence.append(str(line.rstrip() + choice(signoff)))
        shuffle(cat_facts_message_sequence)
        return intro + cat_facts_message_sequence

