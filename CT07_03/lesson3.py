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
print("Addons:
      CountUp:")
addons = input("Which addons do you want to implement? ")
ttime = timer
for i in range(timer):
    time.sleep(1)
    ttime = ttime - 1
    print("You have " + str(ttime) + " minutes left ")