import time as t
import random as r
left = 10
while left != 0:
    t.sleep(1)
    left = left - 1
    if r.randint(1, 20) == 1:
        print("AAAAAAH")
        break
    print(left)
else:
    print("NEW YEAR HAPPY")