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

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets[3] = "J1407b"
planets.append("Plucto")
planets.insert(3, "Land")
planets.insert(6, planets.pop(5))
print(planets)
for i in planets:
    if i == "Earth":
        print("This is not not not not not not my planet")
    elif i == "J1407b":
        print("")