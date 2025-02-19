import random as r
import time as t
selected = []
for i in range(100):
    num = r.randint(1, 1000)
    while num in selected:
        num = r.randint(1, 100)
    selected.append(num)
    print(num)
print(min(selected))
print(max(selected))
print(sum(selected) / len(selected))
print(selected.index(r.choice(selected)))