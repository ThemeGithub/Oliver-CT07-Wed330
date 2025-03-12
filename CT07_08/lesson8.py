while True:
    pw = input("Enter password: ")
    if pw.isupper:
        print("You must have lowercase")
    elif pw.islower:
        print("You must have uppercase")
    elif pw.is