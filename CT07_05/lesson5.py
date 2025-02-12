# food = ["air", "oxygen", "water", "lunch", "dinner"]
# del(food[2])
# # food.pop(2)
# food.append("breakfast")
# for i in food:
#     print(i)

import random as r

nums = []
for i in range(100):
    num = int(str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)))
    while num not in nums:
    nums.append(num)
for i in nums:
    print(i)