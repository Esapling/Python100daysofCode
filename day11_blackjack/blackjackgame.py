import random
import art 

print(art.logo) # you can try logo2 or logo3 as well
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("Welcome to the blackjack card game")
def take_card(player, num):
    """_summary_
        selects randomly "num" number of cards from the "cards" list and appends them 
        to the player(input) list 
        and returns the sum of the cards as integer
        also in the case the total is higher than 21 and selected card is Ace 
        then it returns 1 instead of 11
    Args:
        player (_list_): _a list that have card values as string_
        num (_type_): _number of times to take a card_

    Returns:
        _int_: _the sum of the randomly selected cards' int values _
    """
    total_in_hand = 0
    result = 0
    for card in player:
        total_in_hand += int(card)
    for i in range(num):
        card = cards[random.randint(0,12)]
        player.append(card)
        if card == "11" and total_in_hand + int(card) > 21:
            result += 1
        else:
            result += int(card)
    return result

def play():
    dealer_cards = []
    player_cards = []
    player_score = 0
    dealer_score = 0
    # in each function call these variables should be initalized to empty list and zero
    should_continue = True
    dealer_score += take_card(dealer_cards, 2)
    player_score += take_card(player_cards,2)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    if dealer_score == 21 or player_score == 21: 
        #print("Blackjack")
        should_continue = False
    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_score += take_card(player_cards, 1)                
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {dealer_cards[0]}")
            if player_score >= 21 :
                should_continue = False
            else:
                should_continue = True
        else:
            should_continue = False
    while dealer_score < 17: #if dealer score under than 17 it must take another card
                dealer_score += take_card(dealer_cards , 1)
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    if dealer_score == 21: #even if user also has black jack dealer wins 
        print("Blackjack !! You Lose ")
    elif player_score == 21:
        print("Blackjack You win")
    elif (dealer_score < 21 and dealer_score > player_score) or (player_score > 21 and dealer_score < 21)  or (player_score > dealer_score and player_score > 21):
        print("You lose!")
    elif (player_score < 21 and dealer_score > 21) or (player_score > dealer_score and player_score < 21) or (dealer_score > 21 and dealer_score > player_score):
        print("You win")
    elif player_score == dealer_score:
        print("Draw")
    else:
        print("No more cases left :(")
while True: 
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':")== 'y':
        play()
    else:
        print("Bye.")
        break