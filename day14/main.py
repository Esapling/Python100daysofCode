import art
import random
from game_data import data

print(art.logo)

total_len = len(data)


def print_info(dict_item):
    print(f"{dict_item['name']}, {dict_item['description']}, from {dict_item['country']}")
    
def compare(first, second, ans):
    """checks the user answer and returns if it is true , false otherwise """
    if first['follower_count'] > second['follower_count']:
        return ans == 'A'
    else:
        return ans == 'B'
def play():
    """_summary_
        starts the game and returns the total number of correct anserws 
    Returns:
        _type_: _int_
    """
    total_correct_answ = 0
    while True:
        first = random.choice(data)
        second = random.choice(data)
        if first == second:
            continue  # dont compare the same thing with itself
        print(f"Current score is {total_correct_answ}")
        print(f"Compare A: ",end="")#prevent passing into next line 
        print_info(first)
        
        print(art.vs)
        
        print(f"Against B: ",end="") 
        print_info(second)
        
        ans = input("Who has more followers? Type 'A' or 'B': ")        
        if compare(first, second, ans) == True:
            print("True , Well Done!.")
            total_correct_answ +=1
        else:
            print("Sorry! That is not true")
            return total_correct_answ

       
while True:
    print("Welcome to higher or Lower game.")
    x = play()
    print(f"Your total score is {x}")
    if input("Please Type 'y' to play again ,'n' otherwise: ") == 'n':
        print("Bye.")
        break
    else:
        continue