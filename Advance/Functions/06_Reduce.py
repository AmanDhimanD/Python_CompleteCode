from functools import reduce
# reduce function return sum of all number present in list

sum =lambda a,b:a+b
list1=[1,2,3,4,5,6,7,8,9,10]

function=reduce(sum,list1)
print(function)