# import random
# print("Hero starts on his adventure with Health: 100")
# health = 100
# battles = 0
# while health > 0:
#     battles += 1
#     health = health - random.randint(1, 15)
#     if health <= 0:
#         health = 0
#     print("After fighting monsters, his Health is now: " + str(health))
# print("He fought " + str(battles) + " battles, and died.")


items = []
while True:
    # ask the user what they want
    item = input("What would you like to order? ")
    # end if they say end
    if item == "end":
        break
    else:
        # add the item
        items.append(item)
print("You have ordered the following:")
for i in items:
    print(str(items.index(i) + 1) + ". " + i)