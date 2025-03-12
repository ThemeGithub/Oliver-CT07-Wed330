while True:
    pw = input("Enter password: ")
    if pw.isupper:
        print("You must have lowercase")
    elif pw.islower:
        print("You must have uppercase")
    elif pw.isnumeric:
        print("You must have alphabets")
    elif pw.isalpha:
        print("You must have numbers")
    elif not pw.isalnum:
            print("On")