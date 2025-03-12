while True:
    pw = input("Enter password: ")
    if len(pw) < 8:
        print("It must be 8 characters or longer")
    elif pw.isupper():
        print("You must have lowercase")
    elif pw.islower():
        print("You must have uppercase")
    elif pw.isdigit():
        print("You must have alphabets")
    elif pw.isalpha():
        print("You must have numbers")
    elif not pw.isalnum():
        print("Only alphanumeric characters")
    else:
         break
print("yay")