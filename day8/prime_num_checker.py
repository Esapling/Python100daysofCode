#Write your code below this line 👇
from math import ceil
def prime_checker(number):
    if x == 2:
        print("It's a prime number.")
    x = ceil(pow(number, 0.5))
    flag = True
    for i in range(2,x+1): # no need to check for 1 
        if number % i == 0:
            flag = False
            break
    if not flag:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
