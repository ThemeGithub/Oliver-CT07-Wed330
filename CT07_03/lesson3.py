answer = ""
for i in range(3):
    answer = input("type answer to answer this riddle: ")
    if not answer == "answer":
        print("read the question")
    else:
        break
if answer == "answer":
    print("Correct")