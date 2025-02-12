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
# import random as r
# import math as m
# scores = []
# for i in range(100):
#     scores.append(r.randint(0, 100))

# print(min(scores))
# print(max(scores))
# total = 0
# for i in range(100):
#     total = total + scores[i]
# average = total / 100
# print(average)
# squaretotal = 0
# for i in range(100):
#     squaretotal = (average - scores[i]) ** 2
# avsquare = squaretotal / 100
# print(m.sqrt(avsquare))


# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# print(namelist[heightlist.index(max(heightlist))])
# tallest = max(heightlist)
# while tallest in heightlist
#     del(heightlist[heightlist.index(max(heightlist))])
#     print(namelist[heightlist.index(max(heightlist))])
# print(namelist[heightlist.index(min(heightlist))])

p = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

import random as r
n1 = r.choice(p)
n2 = r.choice(p)
while n2 == n1:
    n2 = r.choice(p)
print(n1)
print("versus")
print(n2)
n1p = powers[p.index(n1)]
n2p = powers[p.index(n2)]
if n1p >= r.randint(1, n1p + n2p):
    print(n1p)
else:
    print(n2p)