from replit import clear

#HINT: You can call clear() to clear the output in the console.
from art import logo 
print(logo)
# print logo to the console


# an empty dict to store each person with their offers
auction = {}

# a flag to keep control of the flow
while True:
    print("Welcome to the secret auction program. ")
    name = input("What is your name? ")
    bid = int(input("What's your bid?: "))
    auction[name] = bid
    opt = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if opt == "yes":
        clear()# for windows import os and use os.system("cls") or os.system("clear") for linux 
        continue
    else:
        break

# calculate the highest bid to find winner 
max = 0
max_bidder = ""
for bidder in auction:
    if auction[bidder] > max:
        max_bidder = bidder
        max = auction[bidder]

print(f"The winner is {max_bidder} with a bid of ${max}")



