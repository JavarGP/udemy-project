
# this code encrpyts a message by using a ceasar cypher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = [' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ',']

purpose = input (" would you like to hide or unhide a message?\n ")

if (purpose == "hide"):
  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  def encrypt(text, shift):

    word_to_list = list(text)
    x = text.split(' ')


    def myfunc(a):
      return len(a)
    t = map(myfunc, x)
    spacing = map(myfunc, x)
    spacer = list(spacing)
  

    list_container1 = []
    for a in word_to_list:
      if a == " ":
        continue
      b = alphabet.index(a)
      list_container1.append(b)
    b
    x = alphabet
    for x in range(shift):
      letter_list = alphabet
      letter_remove = letter_list.pop(0)
      alphabet.append(letter_remove)

    list_container2 = []
    for a in list_container1:
      conversion = alphabet[a]
      list_container2.append(conversion)
      list_to_string = ''.join(list_container2)
    list_to_string


    res = []
    for split in spacer:
      temp=list_to_string[:split]
      list_to_string = list_to_string[split:]
      res.append(temp)
    t = ' '.join(res)
    print(t)
    return t
  encrypted = encrypt(text, shift)

# this code decode the encryption
elif (purpose == "unhide"):
  
  changer = input("Would you like to translate a message:\n ").lower()
  reverter = int(input("Type the shift number:\n"))

  def decode(changer, reverter):

    inverter = (len(alphabet) - reverter)    
    word_to_list = list(changer)
    x = changer.split(' ')

    def myfunc(a):
      return len(a)
    t = map(myfunc, x)
    spacing = map(myfunc, x)
    spacer = list(spacing)
  

    list_container1 = []
    for a in word_to_list:
      if a == " ":
        continue
      b = alphabet.index(a)
      list_container1.append(b)
    b
    x = alphabet
    for x in range(inverter):
      letter_list = alphabet
      letter_remove = letter_list.pop(0)
      alphabet.append(letter_remove)

    list_container2 = []
    for a in list_container1:
      conversion = alphabet[a]
      list_container2.append(conversion)
      list_to_string = ''.join(list_container2)
    list_to_string


    res = []
    for split in spacer:
      temp=list_to_string[:split]
      list_to_string = list_to_string[split:]
      res.append(temp)
      t = ' '.join(res)
    print(t)
    return t 
  decoded = decode(changer, reverter)
else :
  print("try again")