import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess_char = input("Guess one character: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# def find(string , x):
#     for i in string:
#         if i == x:
#             return True
#     return False
# if find(chosen_word, guess_char) == True:
#     print("Right")
# else:
#     print("Wrong")
# print(f"Chosen word is {chosen_word}")

for l in chosen_word:
    if guess_char == l:
        print("Right")
    else:
        print("Wrong")