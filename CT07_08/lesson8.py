while True:
    pw = input("Enter password: ")
    if not pw.isupper and not pw.islower and pw.isalnum and not pw.isalpha and not pw.isnumeric:
        break
    else:
        print("Your password must have uppercase, lowercase, alpha")