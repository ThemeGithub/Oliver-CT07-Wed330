import random as r
import time as t
selected = []
for i in range(100):
    num = r.randint(1, 1000)
    while num not in selected:
        num = r.randint(1, 100)
    selected.append(num)