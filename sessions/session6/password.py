while True:
    password = input("enter your password: ")
    if password.isalpha():
        print("must contain number")
    elif len(password) <= 8:
        print("must have more than 8 characters")
    else:
        print("done")
        break