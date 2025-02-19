import random as r
import time as t
# selected = []
# for i in range(100):
#     num = r.randint(1, 1000)
#     while num in selected:
#         num = r.randint(1, 100)
#     selected.append(num)
#     print(num)
# print(min(selected))
# print(max(selected))
# print(sum(selected) / len(selected))
# ran = r.choice(selected)
# print(ran)
# print(selected.index(ran))

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)
# for i in contacts:
#     for j in i:
#         print(j)

# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# boys = []
# girls = []
# for i in students:
#     name, gender = i
#     print(name + ": " + gender)
#     if gender == "F":
#         boys.append(name)
#     else:
#         girls.append(name)
# print("Boys:")
# for i in boys:
#     print(i)
# print("Girls:")
# for i in girls:
#     print(i)
# print("Boys " +str(len(boys)))
# print("Girls " +str(len(girls)))

people = []
numbers = []
while True:
    name = input("What is your name? ")
    if name == "end":
        break
    gender = input("What is your gender? ")
    number = r.randint(0, 1000)
    while number in numbers:
        number = r.randint(0, 1000)
    numbers.append(number)
    print("Your number is " + str(number))
    people.append([name, gender, number])
winner = random.choice(numbers)
print("The winner is... ")
t.sleep(1)
for i in str(winner):
    print(i)