import random
from  dictionary_HighLowGame import data 

x = random.choice(data)
y = random.choice(data)

k = 0
while k < 1:
    guess1 = input(f"Is {x['name']} higher or lower then {y['name']}? ")

    if guess1 == "higher" and x["follower_count"] > y["follower_count"]:
        print("Excellent")
        
    elif guess1 == "lower" and x["follower_count"] < y["follower_count"]:
        print("Great")
    else:
        print("Sorry you lose")
        k += 1