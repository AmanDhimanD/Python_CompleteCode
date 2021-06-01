# count() Method
item=(1,2,3,4,4,5,6,6,7,7,7,7,5,4,4,6,7,2,3)
#Here,we use f-string 
print(f"Number of 2 is {item.count(2)}")
print(f"Number of 3 is {item.count(3)}")
print(f"Number of 4 is {item.count(4)}")
print(f"Number of 5 is {item.count(5)}")
print(f"Number of 6 is {item.count(6)}")
print(f"Number of 7 is {item.count(7)}")

#index() Method
print(item.index(7)) #index-->8
print(item.index(71)) #Throw an error
    