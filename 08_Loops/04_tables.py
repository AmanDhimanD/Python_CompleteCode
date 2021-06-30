number=int(input("Enter number of table:-"))
for i in range (1,number):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
    print("\n")