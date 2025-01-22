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

import time
timer = int(input("How many minutes is the timer? "))
print("Addons:")
print("CountUp: Counts up, instead of down")
print("Hours: Takes in hours instead of minutes")
print("Seconds: Takes in seconds instead of minutes")
print("Stopwatch: Tells you how much time there is every minute, no timer")
addon = input("Which addons do you want to implement? ")
timeunit = "minutes"
ttime = timer
for i in range(timer):
    if addon == "Hours":
        time.sleep(3600)
        timeunit = "hours"
    elif addon == "Seconds":
        time.sleep(1)
    else:
        time.sleep(60)
    ttime = ttime - 1
    if addon == "CountUp":
        print("You have " + str(timer - ttime) + " " + timeunit + " left")
    else:
        print("You have " + str(ttime) + " " + timeunit + " left")
print("TIMES UP")