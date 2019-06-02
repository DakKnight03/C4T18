password = input("enter your password: ")
while True:
    re_pass = input("re-enter your password: ")
    if re_pass == password:
        print("done")
        break
    else:
        print("error")