# calculator 
import art 
print(art.logo)
def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multp(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        exit("\nError division by 0 is not valid") # this will cause the program to end
    return n1 / n2
def exponent(n1, n2):
    return n1**n2
operations = {
    "+" : add,
    "-" : subtract,
    "*": multp,
    "/":divide,
    "^":exponent,
}

def calc():
    n1 = float(input("What is the first number?: "))
    while True:
        for symbol in operations:
            print(symbol)
        opr = input("Pick an operation :")
        n2 = float(input("What is the next number?: "))
        fun = operations[opr]
        result = fun(n1,n2)
        print(f"{n1} {opr} {n2} =  {result}")
        flag = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculator or exit to exit the program: ")
        if flag == "y":
            n1 = result
            continue
        elif flag == "n":
            calc()
            break
        else:
            break
    print(f"Result is : {result}")
calc()