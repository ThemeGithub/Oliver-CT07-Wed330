import random
print("Hero starts on his adventure with Health: 100")
health = 100
battles = 0
while health > 0:
    battles += 1
    health = health - random.randint(1, 15)
    if health <= 0:
        health = 0
    print("After fighting monsters, his Health is now: " + str(health))
print("He fought " + str(battles) + " battles, and died.")