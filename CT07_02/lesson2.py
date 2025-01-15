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

# items = []
# while True:
#     item = input("I want ")
#     items.append(item)
#     if input("Is that all? ") == "Yes":
#         break
# money = 15
# print("You ordered ")
# for i in items:
#     print(i)
#     money += 2
# print("Your total money is $" + str(money))

questions = [
    "Are you dumb ", "What is 1 + 1 ", "What is the color of the sky "
]
answers = [
    "yes", "10", "cyan"
]
question = 0
ans = ""
while question != 3:
    while ans != answers[question]:
        ans = input(questions[question])
        if ans != answers[question]:
            print("boo")
    else:
        print("yay")
    question += 1

'''
## Task 5: General Knowledge Quiz
**Task: Create a program to quiz users on their general
knowledge**

Using the while loop, ask 3 general knowledge questions
1. Using input ask the question
2. While answer is not correct, repeat the question.
3. Move on to the next question when the answer is correct

Bonus:
1. Add a score system
2. Add an ability for users to skip by saying “skip”
3. Disqualify user when they have tried too many times

'''
