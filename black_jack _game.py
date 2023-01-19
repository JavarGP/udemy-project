from ascii_art import logo
import random 

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

pick_card = random.choices(cards, k = 2)
 
dealers_hand = []
player_hand = []

def cards_hand():
  a = pick_card
  return a 
a = cards_hand()  


for b in a:
  b = random.choices(cards, k = 2)
  
  
players = {
  "player_1" : a,
  "dealer" : b,
}

print(players["player_1"], b[0])
switch = True
while  switch == True :
  hit = input("Do you want to get another card? ")
  y = hit.lower()
  print(y)

  d = random.choice(cards)
  dealers_hand = [b]
  
  

  if hit == "yes":
    for player_hand in range(1) :
      c = random.choice(cards)
      a.append(c)
    print(a)
       
  elif sum(a) > 21:
    print(f"sorry you lost! {sum(a)}")
    switch = False
  elif sum(a) == 21:
    print(f"You aced it {sum(a)}")
  elif sum(b) <= 17:
    b.append(d)
    sum(b)
    swtich = False
  elif sum(a) > sum(b) and sum(a) <= 21 or sum(b) > 21:
    print(f"You win!!!{sum(a)} {sum(b)}")
    switch = False
  elif sum(b) < sum(a) and sum(b) <= 21 :
    print(f"Sorry the house won {sum(b)}")
    switch = False
  elif sum(a) == sum(b):
    print(f"Its a draw {sum(a)} {sum(b)}") 
    switch = False
  else :
    switch = False