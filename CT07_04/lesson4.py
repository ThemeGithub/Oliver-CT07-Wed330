# import time as t
# import random as r
# left = 10
# while left != 0:
#     print(left)
#     t.sleep(1)
#     left = left - 1
#     if r.randint(1, 20) == 1:
#         print("AAAAAAH")
#         break
# else:
#     print("NEW YEAR HAPPY")

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
# planets[3] = "J1407b"
# planets.append("Plucto")
# planets.insert(3, "Land")
# planets.insert(6, planets.pop(5))
# for i in planets:
#     if i == "Earth":
#         print("Eart: This is not not not not not not my planet")
#     elif i == "J1407b":
#         print("b7041J: COnquerer: me, yay")
#     elif i == "Land":
#         print("Land: made in china (me)")
#     else:
#         print(i)

# countries = []
# while True:
#     country = input("Where do vyou go ")
#     if country == "end":
#         break
#     countries.append(country)
# for i in countries:
#     print("i want to not not go " + i)


food = []
price = []
while True:
    item = input("What do vyou eat ")
    if item == "end":
        break
    food.append(item)
    food.append(input("how much does it prcie"))
for i in food:
    print("i want to not not add " + i)
order = input("order what ")
# if order in food:
#     print("we have that")
# else:
#     print("we dont have")
for i in food:
    if i == order:
        print("we have")
        break
else:
    print("go away")