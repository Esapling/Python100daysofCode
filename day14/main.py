import art
import random
from game_data import data

print(art.logo)

total_len = len(data)


def print_info(index):
    print(f"{data[index]['name']}, {data[index]['description']}, from {data[index]['country']}")
    
def compare(index1, index2):
    if data[index1]['follower_count'] > data[index2]['follower_count']:
        true_ans = 'A'
    else:
        true_ans = 'B'
    ans = input("Who has more followers? Type 'A' or 'B': ")        
    if ans == true_ans:
        print("True! You got this.")
        return True
    else:
        print("Sorry!")
        return False
def play():
    """_summary_
        starts the game and returns the total number of correct anserws 
    Returns:
        _type_: _int_
    """
    result = True
    total_correct_answ = 0
    while result:
        first = random.randint(0, total_len - 1)
        second = random.randint(0, total_len - 1)
        if first == second:
            continue  # dont compare the same thing with itself
        print(f"Compare A: ",end="")#prevent passing into next line 
        print_info(first)
        
        print(art.vs)
        
        print(f"Compare B: ",end="") 
        print_info(second)
        if compare(first, second) == True:
            total_correct_answ +=1
        else:
            return total_correct_answ
        
       
while True:
    print("Welcome to higher or Lower game.")
    x = play()
    print(f"Your total score is {x}")
    if input("Please Type 'y' to play again ,'n' otherwise: ") == 'n':
        print("Bye.")
        break
    
    