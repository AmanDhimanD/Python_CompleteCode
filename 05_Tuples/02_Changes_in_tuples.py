""" Tuple cannot be change if we want to change in tuple so 
we have to make it list first 
then we can change 
"""
tup = ("a", "b", "c")
# convert into list
y = list(tup)
# change at 2nd index
y[2] = "Change"
# again in tuple
tup = tuple(y)
# print
print(tup)

""" 
These are also exits
Append
Remove 
Delete 
"""