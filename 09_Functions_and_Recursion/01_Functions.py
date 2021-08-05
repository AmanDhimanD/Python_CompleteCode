# Functions Decleration
def function1(name):
    print(f"Hello Good Morning ,Mr. {name} Sir.")
    
def function2(age,id_number):
    final=print(f"\nAge is {age} and ID number is {id_number}.")
    return final


name=(input("Enter your name :- "))
#Function calling 
greet=function1(name) 
print(greet) 
age=int(input("What is your age ? "))
id=int(input("Enter your id number :- "))
print(function2(age, id))
