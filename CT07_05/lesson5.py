# food = ["air", "oxygen", "water", "lunch", "dinner"]
# del(food[2])
# # food.pop(2)
# food.append("breakfast")
# for i in food:
#     print(i)

# import random as r

# nums = []
# for i in range(100):
#     num = int(str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)))
#     while num in nums:
#         num = int(str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)))
#     nums.append(num)
# for i in nums:
#     print(i)
# print(int(input("choose num ")) in nums)
import random as r
scores = []
for i in range(100):
    scores.append(r.randint(0, 100))

print(min(scores))
print(max(scores))
total = 0
for i in range(100):
    total = total + scores[i]
average = total / 100
print(average)
squaretotal = 0
for i in range(100):
    squaretotal = (average - scores[i]) ** 2
avsquare = squaretotal / 100
print()