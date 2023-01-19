import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

u = []
v = []
w = []

for x in range (0, nr_letters):
  x = random.choice(letters[0: -1])
  w += str(x)
 
for y in range (0, nr_numbers):
  y = random.choice(numbers[0: -1])
  v += y

for z in range (0, nr_symbols):
  z = random.choice(symbols[0: -1])
  u += z
  
t = list(w + v + u)
random.shuffle(t)
str1 = ''.join(str(e) for e in t)

print(f"Your password is {str1}")