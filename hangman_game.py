from operator import index
from os import remove
from posixpath import split
import random
from re import T
from xml.dom.pulldom import END_DOCUMENT
import random

fruits = [['a','p','p','l','e'], ['o','r','a','n','g','e'], ['b','a','n','a','n','a']]
animals = [['c','a','m','e','l'], ['s','n','a','k','e'], ['v','u','l','t','u','r','e'], ['c','e','n','t','e','p','e','d','e']]
trees = [['m','a','h','o','g','a','n','y'], ['p','i','n','e'], ['b','i','r','c','h']]

fruit = random.choice(fruits)
animal = random.choice(animals)
tree = random.choice(trees)

mylist = [fruit, animal, tree]
random_listed_word = random.choice(mylist)
# print(random_listed_word)

the_word = len(random_listed_word)*["_"]
incorrect_guesses = []
q = 0
free_space = the_word.count("_")

while free_space != 0 and len(incorrect_guesses) < 5:
    
    guess = input("What is your guess? ")
    
    for x in random_listed_word:
        if x != guess:
            for i in range(len(random_listed_word)):
                if random_listed_word[i] == guess:
                    the_word[i] = random_listed_word[i]
    
    incorrect_guesses.append(guess)


    free_space = the_word.count("_")
    print(free_space)
    if free_space == 0: 
        print("You win!")        
    print(the_word)
      
    for x in random_listed_word:
            if x == guess:
                incorrect_guesses.remove(guess)
                break 
                q += 1         
    print(incorrect_guesses)  
    print(f"You have {5 - len(incorrect_guesses)} guesses left")
if len(incorrect_guesses) == 5:
    print("sorry you lose")