import art 
print(art.logo)
import random



print("Welcome to the Guess The Number game\nI am thinking of a number between 1 and 100 ")
level = input("To select a diffulty level type 'easy' or 'hard': ")

if level == 'easy':
    attemptNo = 10
else:
    attemptNo = 5

number = random.randint(1,100)
while attemptNo > 0:
    print(f"You have {attemptNo} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    attemptNo -=1
    if guess == number:
        break
    elif guess < number:
        print("Too low\nGuess again")
    elif guess > number:
        print("Too high\nGuess again")


if attemptNo == 0:
    print(f"Sorry you dont have any attempt left ,Number was the{number}")
elif attemptNo > 0:
    print("Well done you have found the correct number")