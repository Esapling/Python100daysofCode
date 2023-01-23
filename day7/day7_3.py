#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
def find(list , x):
    for i in list:
        if x == i:
            return True
    return False


while find(display,"_"):
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(display)
print("You win")

# another possible solution 
# creating a flag var and 
# if "_" not in list:
#     flag == true end of game
#  flag = true
# while flag:
#     guess = input("Guess a letter: ").lower()
#     for i in range(len(chosen_word)):
#         if guess == chosen_word[i]:
#             display[i] = guess
#     print(display)
#     if "_" not in display:
#        flag = false // end of the loop 
#        print("You win")