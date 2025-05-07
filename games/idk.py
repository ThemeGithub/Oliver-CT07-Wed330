'''
Have you played Wordle before? Try it out here >> Wordle - The New York Times (nytimes.com)

In this assignment, you are given a text file containing 5757 5-letter words. 

In this assignment, your task is to create a program that works like wordle. Your program will:

1. Choose a random word from the list

2. Allow you to input a 5-letter word

3. Validate if you have you have the letter in the correct position, correct letter but in the wrong position, or the wrong letter.

4. You can use the console output to print out the statements
'''
import random

with open("wordlist.csv", 'r') as file:
    words = file.read()
    wordlist = words.split(",")

def getword():
    while True:
        sent = input("guess: ")
        if len(sent) != 5:
            print("it must be 5 letter")
        elif not sent in wordlist:
            print("make a good word bro")
        else:
            return sent.upper()

def checkword(guess, word):
    string = ''
    for i in range(5):
        if guess[i] in word:
            if guess[i] == word[i]:
                string = string + guess[i]
            else:
                string = string + '?'
        else:
            string = string + '#'
    return string

word = (random.choice(wordlist)).upper()
for i in range(6):
    guess = getword().upper()
    print(guess)
    print(checkword(guess, word))
    if word == guess:
        print("you cheated and won")
        break
else:
    print('you are dum')
    print(word)