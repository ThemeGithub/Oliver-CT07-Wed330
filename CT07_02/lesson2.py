# import random

# score = 0
# for i in range(10):
#     n1 = random.randint(2, 6)
#     n2 = random.randint(2, 4)
#     while True:
#         ans = int(input(f'{n1} ^ {n2} = '))
#         if ans == n1**n2:
#             print("Correct, + 1000")
#             score += 1000
#             break
#         else:
#             print("Wrong, - 1000")
#             score -= 1000

# print(score)

items = []
while True:
    item = input("I want ")
    items.append(item)
    if input("Is that all? ") == "Yes":
        break
money = 15
for i in items:
    print(i)
    money += 2
print("Your total money is $" + str())