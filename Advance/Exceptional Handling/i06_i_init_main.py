def greet(name):
    x=name.upper()
    print(f"Good Job !! {x}. ")

#name print only in the self file not in the another module throught the import
if __name__=="__main__":
    n=input("Name :- ")
    greet(n)