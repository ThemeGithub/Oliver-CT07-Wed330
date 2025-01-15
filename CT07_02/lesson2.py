import random

n1 = random.randint(2, 6)
n2 = random.randint(2, 4)
while True:
    ans = int(input(f'{}'))
    if ans == n1**n2:
        print("Correct")
        break
    else:
        print("wrong")