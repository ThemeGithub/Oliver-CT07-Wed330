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
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':1}

# deck = [(rank, suit) for rank in ranks for suit in suits]
deck = []
player = []
banker = []
# Combine ranks and suits to build a deck of cards
for suit in suits:
    for rank in ranks:
        deck.append([rank, suit])

diff = input('Choose a difficulty; Pick between 1 and 10: ')
diff = round(int(diff))

# Step 2: Shuffle the deck
for i in range(10):
    random.shuffle(deck) # shuffle this 10 times


def showhand(hand, type):
    sum = points(hand)
    if type == "player" or type == "end":
        print("#" * 10)
        if type == 'player':
            print("PLAYER HAND")
        else:
            print('BANKER HAND')
        for card in hand:
            print(f'{card[1]} {card[0]}')
        print(f'Sum: {sum}')
        print('#' * 10)
    elif type == "banker":
        print('$' * 10)
        print("BANKER HAND")
        if diff >= 8:
            for i in range(2):
                print("?????")
        else:
            print(f'{hand[0][1]} {hand[0][0]}')
            print('?????')
        print('$' * 10)

def points(hand):
    aces = 0
    sum = 0
    for card in hand:
        cardpoint = values[card[0]]
        sum += cardpoint
        if card == 'ACE':
            aces += 1
    for i in range(aces):
        if sum <= 11:
            sum += 10
    return sum

def bankermove(hand):
    end = 0
    while end == 0:
        sum = points(hand)
        if diff == 1:
            if sum < 20:
                banker.append(deck.pop())
            else:
                end = 1
        if diff == 2:
            if sum < 19:
                banker.append(deck.pop())
            else:
                end = 1
        if diff == 3:
            if sum < 18:
                banker.append(deck.pop())
            else:
                end = 1
        if diff == 4:
            if sum < 17:
                banker.append(deck.pop())
            else:
                end = 1
        if diff == 5 or diff == 6:
            if sum < 16:
                banker.append(deck.pop())
            else:
                end = 1
        if diff > 6:
            left = 21 - sum
            fail = 0
            for card in deck:
                if values[card[0]] > left:
                    fail += 1
            if fail > 0:
                if fail / len(deck) < 0.2 + diff * 0.05:
                    banker.append(deck.pop())
                else:
                    end = 1
            else:
                banker.append(deck.pop())
        if end == 0:
            showhand(hand, "end")
        time.sleep(1.2)
        print("")
    return banker

            
        

player = [deck.pop(), deck.pop()]
banker = [deck.pop(), deck.pop()]

showhand(banker, "banker")
showhand(player, "player")

while True:
    print("1: Hit")
    print("2: Check")
    if input("Choose your move: ") == '1':
        player.append(deck.pop())
    else:
        break
    showhand(banker, 'banker')
    showhand(player, "player")

bankervalue = points(bankermove(banker))
showhand(player, 'player')
playervalue = points(player)
if bankervalue > playervalue:
    if bankervalue <= 21:
        print("Banker WINS! YOU SUCK LOLOLOLOLOL")
    else:
        if playervalue <= 21:
            print("banker too addicted and lost cuz he go over")
        else:
            print('you suck less than banker')
            print('you still suck tho')
elif bankervalue < playervalue:
    if playervalue <= 21:
        print("cheater")
    else:
        if bankervalue <= 21:
            print('IMAGINE GOING OVER LOLOLOLO')
        else:
            print('uhh')
            print('u still suck more tho')
else:
    if bankervalue <= 21:
        print('its a tie')
    else:
        print('both of u suck')
    print('boringgggg')