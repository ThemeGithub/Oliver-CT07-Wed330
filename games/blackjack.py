'''
Create the game of Black Jack
'''
import random
import time

suits = ["♣", "♦","♡","♠"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}

# deck = [(rank, suit) for rank in ranks for suit in suits]
deck = []
player = []
banker = []
# Combine ranks and suits to build a deck of cards
for suit in suits:
    for rank in ranks:
        deck.append([rank, suit])

diff = input('Choose a difficulty; Pick between 1 and 10')
diff = round(diff)

# Step 2: Shuffle the deck
for i in range(10):
    random.shuffle(deck) # shuffle this 10 times


def showhand(hand, type):
    if type == "player":
        for card in hand:
            print(f'{card[1]} {card[0]}')
    elif type == "banker":
        if diff >= 8:
            for i in range(2):
                print("?????")
        else:
            print(f'{card[1]}')



player = [deck.pop(), deck.pop()]
banker = [deck.pop(), deck.pop()]

showhand(player, "player")