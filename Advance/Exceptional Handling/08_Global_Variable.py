a=34 #Global Variable 
def scope():
    global a
    print(f"\nBefore Change the value of global variable :- {a}")
    a=45 #1.Local Variable
         #2.Change the global variable
    print(f"\nAfter Change the Value of a:-{a}")

scope()
print(f"\n{a}") #after change value of a 