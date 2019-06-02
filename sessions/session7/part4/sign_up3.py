while True:
    email = input("enter your email: ")
    if "@" and "." in email:
        print("valid email")
        break
    else:
        print("invalid email")
    
while True:
    password = input("enter your password: ")
    if len(password) <= 8 or password.isalpha():
        print("enter a valid password: more than 8 characters and have both numbers and letters")
    else:
        print("valid password")
        break