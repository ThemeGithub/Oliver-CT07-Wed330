# import turtle
# window = turtle.Screen()
# window.setup(width = 600, height = 400)

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("orange")

# def square():
#     for i in range(4):
#         t.forward(100)
#         t.left(90)


# square()


# window.mainloop()

# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(3, 5))

# import random

# numbers = []
# for i in range(100):
#     num = random.randint(80000000, 99999999)
#     while num in numbers:
#         num = random.randint(80000000, 99999999)
#     numbers.append(num)


# def talktome(number):
#     return("https://waa.mee/65" + number)



# for i in range(100):
#     print(talktome(str(numbers[i])))


import random
nums = []
for i in range(100):
    nums.append(i + 1)

picked = []
def randgen(amount):
    for i in range(amount):
        pick = random.choice(nums)
        del(nums[nums.index(pick)])

randgen(int(input("how many ")))
print("highest = " + str(max(picked)))
print("lowest = " + str(min(picked)))
print("amount = " + str(len(picked)))
print("average = " + str((sum(picked) / len(picked))))