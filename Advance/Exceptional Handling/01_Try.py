while (True):
    print("press q to exit....")
    a=input("Enter a number:- ")
    if a=="q":
        break
    try:
        a=int(a)
        if a>8:
            print("Number is grather than 8")
        elif a<8:
            print("Number is smaller than 8")
    except Exception as e:
        print(f"You input is wrong {e}")
