import random

while True:
    n1 = random.random(2, 6)
    n2 = random.random(2, 4)
    ans = int(input(str(n1) + "^" + str(n2)))
    if ans == n1**n2:
        print("Correct")
        break
    else:
        print("wrong")