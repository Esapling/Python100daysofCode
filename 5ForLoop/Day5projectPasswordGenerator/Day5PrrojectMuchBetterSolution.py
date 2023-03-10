#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# lenLetter = len(letters)
# lenSymb = len(symbols)

# password = ""
# for x in range(0, nr_letters):
#     a = random.randint(0, lenLetter-1)
#     password += letters[a]

# for x in range(0, nr_numbers):
#     a = random.randint(0, 9)
#     password += numbers[a]
# for x in range(0, nr_symbols):
#     a = random.randint(0,lenSymb-1)
#     password += symbols[a]

# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# lenLetter = len(letters)
# lenSymb = len(symbols)

passwordList = []
for x in range(1, nr_letters+1):
    #a = random.randint(0, lenLetter-1)
    passwordList.append(random.choice(letters))
for x in range(1, nr_symbols+1):
    #a = random.randint(0,lenSymb-1)
    #password += random.choice(symbols)    
    passwordList.append(random.choice(symbols))
    
for x in range(1, nr_numbers+1):
    #password += random.choice(numbers)
    passwordList.append(random.choice(numbers))

#password = list(password)
random.shuffle(passwordList)
password = ""
for char in passwordList:
    password += char
#password = ''.join(passwordList)
print(password)
