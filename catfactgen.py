from random import choice

signoff = [' Luv, CatFacts!', ' Awesome!', ' TO STOP REPLY <STOP>', ' This is Catsfacts!']

def generate_cat_facts():
	outlist =[]
	with open("catfacts.txt") as file:
		for line in file:
			outlist.append(str(line.rstrip() + choice(signoff)))
		return outlist
