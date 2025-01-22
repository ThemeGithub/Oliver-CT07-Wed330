import random
hints = {"read the question", "it starts with 'A'", "it ends with 'R'", }
answer = ""
for i in range(3):
    answer = input("type answer to answer this riddle: ")
    if not answer == "answer":
        print("read the question")
    else:
        break
if answer == "answer":
    print("Correct")
else:
    print("u are dumb")