from data import MENU
from data import resources

total_money_in_machine = 0


def make_beverage(choice):
    """rearranges resources in hand processing the desired beverage sources"""
    ingredients = choice['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
        

def check_sources(beverage):
    """ returns true if sources are enough, false otherwise """
    ingredients = beverage['ingredients']
    for ingredient in ingredients:
        #ingredient like water cofffee etc
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return 0.25 * quarters + pennies * 0.01 + nickles * 0.05 + dimes * 0.1


def coffee_machine():
    # TODO 1 Ask user to what he wants
    flag = True
    global total_money_in_machine
    while flag:
        beverage = input("What would you like?: (Latte/Espresso/Caffe), please type 'off' to end the program or report to see resources: ").lower()
        if beverage == 'off':
            return
        elif beverage == 'report':
            for i in resources:
                print(f"{i} : {resources[i]}")
                print(f"profit : ${total_money_in_machine}")
            continue
        # TODO 1.2 Check if resources are enough
        elif not check_sources(MENU[beverage]):
            #  if there is not enough sources dont proceed
            #  menu[beverage] is a dict of the beverage
            continue
        # TODO 2 Give info about cost of the hot beverage  Ask user to put money
        else:
            choice = MENU[beverage]
            print(f"{beverage} will cost {choice['cost']}")
            print("Please insert coins")
            total = process_money()
        # TODO 3 Check the money if not enough then give the money back and return the first case

            if total < choice['cost']:
                print("Not enough money! Money refunded !!!")
                continue
                # return #
            else:
                change = round(total-choice['cost'])
                total_money_in_machine += choice['cost']
                print(f"Here {change} in change")
                make_beverage(choice)
                print(f"Here is your {beverage} .Enjoy")

coffee_machine()