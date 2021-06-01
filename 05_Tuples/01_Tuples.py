# tuple is immutable (cann't change)
#Duplicates are allow
tup=("rayne","github","Coder","Hello")
print(tup)

# difference between List VS. Tuples
a= (1,2,3,4,5,6,7,8,9,0) #Tuples
b= [1,2,3,4,5,6,7,8,9,0] #Lists

print('a=',a.__sizeof__())
print('b=',b.__sizeof__())  