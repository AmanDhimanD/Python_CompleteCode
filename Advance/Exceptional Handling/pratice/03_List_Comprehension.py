while (True):
    print("Enter q for Exit.....")
    try:
        n=int(input("Enter Number for Table:- "))
        if n=='q':
            break
        else:
            table=[n*i for i in range(1,11)]
            print(table)
    except ValueError as e:
        print("Some Mistake Occure")
        break