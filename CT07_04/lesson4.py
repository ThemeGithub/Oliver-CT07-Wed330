import time as t
import random as r
left = 10
while left != 0:
    t.sleep(1)
    t = t - 1
    if r.randint(1, 10) == 1:
        print("AAAAAAH")
        break
else:
    