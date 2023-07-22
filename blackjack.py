#################### SIMPLE BLACK JACK RULES #########################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn
# Automatic black jack = A hand with only 2 cards: ace + 10. as the score will be 21


import random
import os
from blackjack_art import logo

def deal_card():
    "Returns a random card from the deck"
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    # first thing, check for an automatic blackjack. Return 0, as it will represent black jack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #The Ace can count as 11 or 1. if the score is already over 21, then the program should remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# the program has to compare both the user's hand and the computer's hand to determine the winner
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You Lose 😤"
    

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 💥"
    elif user_score == 0:
        return "You win with a Blackjack 👊"
    elif user_score > 21:
        return "You went over, You Lose! ❌"
    elif computer_score > 21:
        return "Computer went over, You win! ⛳"
    elif user_score > computer_score:
        return "You win 🥂"
    else:
        return "You Lose 😭"
    
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    still_playing = True

    for _ in range(2):
        user_cards.append(deal_card())    
        computer_cards.append(deal_card())

    # The score needs to be checked with each hand
    while still_playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    You cards: {user_cards}, current score: {user_score}")
        # only display one card for the computer's hand
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            still_playing = False
        else:
            # if in the first round, there is no winner, the game should continue till the winning deck is established
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    still_playing = False
    
    # Once user has opted to get another card, it is time to let the computer play if the program has not ended with a black jack already
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer;s final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Allow the user to restart the game if they want to or end it
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system("cls")
    play_game()

