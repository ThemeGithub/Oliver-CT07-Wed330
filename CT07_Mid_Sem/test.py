import random as r
print("Hero starts on his adventure with Health: 100")
health = 100
while health > 0:
    health = health - r.randint(1, 15)
    print("After fighting monsters, his Health is now: ")