# import random
# hints = ["read the question", "it starts with 'A'", "it ends with 'R'", "it has 2 voewls", "it is in the question"]
# answer = ""
# for i in range(3):
#     answer = input("type answer to answer this riddle: ")
#     if not answer == "answer":
#         hint = random.randint(1, len(hints))
#         print(hints[hint])
#         hints.pop(hint)
#     else:
#         break
# if answer == "answer":
#     print("Correct")
# else:
#     print("u are dumb")

# import time
# timer = int(input("How many minutes is the timer? "))
# print("Addons:")
# print("CountUp: Counts up, instead of down")
# print("Hours: Takes in hours instead of minutes")
# print("Seconds: Takes in seconds instead of minutes")
# print("Stopwatch: Tells you how much time there is every minute, no timer")
# addon = input("Which addons do you want to implement? ")
# if addon == "Stopwatch":
#     addon = "CountUp"
#     timer = 99999999**99999999**9999999999**9999999999**999999999**9999999**999999999
# timeunit = "minutes"
# ttime = timer
# for i in range(timer):
#     if addon == "Hours":
#         time.sleep(3600)
#         timeunit = "hours"
#     elif addon == "Seconds":
#         time.sleep(1)
#         timeunit = "seconds"
#     else:
#         time.sleep(60)
#     ttime = ttime - 1
#     if addon == "CountUp":
#         print("You have " + str(timer - ttime) + " " + timeunit + " left")
#     else:
#         print("You have " + str(ttime) + " " + timeunit + " left")
# print("TIMES UP")
# money = 0
# while True:
#     add = int(input("How much did you save today?"))
#     money = money + add
#     if money >= 100:
#         print("you saved $100, time to go for $1000!")
#         break

# while True:
#     add = int(input("How much did you save today?"))
#     money = money + add
#     if money >= 1000:
#         print("you saved $1000, time to go for $10000!")
#         break

# while True:
#     add = int(input("How much did you save today?"))
#     money = money + add
#     if money >= 10000:
#         print("you saved $10000, time buy a house!")
#         break
    
# import random as r
# min = 10
# max = 50
# lives = 3
# answer = 0
# for i in range(15):    
#     a1 = r.randint(2, 20)
#     a2 = r.randint(2, 20)
#     while a1 * a2 > max or a1 * a2 < min:
#         a1 = r.randint(2, 20)
#         a2 = r.randint(2, 20)
#     while answer != a1 * a2:
#         answer = int(input("What is " + str(a1) + " * " + str(a2) + "? "))
#         if answer != a1 * a2:
#             print("Wrong, try again!")
#             lives = lives - 1
#             min = min * 0.75
#             max = max * 0.7
#         else:
#             print("yay, correct")
#             min = min * 2
#             max = max * 1.75
#             if min > 350:
#                 min = 350
#             break
#         if lives <= 0:
#             break
#     if lives <= 0:
#         print("GO AND SEE TEACHER I FORGOT NAME")
#         break
