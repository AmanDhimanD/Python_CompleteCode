list = [1,4,5,67,345,780]


# b = []
# for item in list:
#    if item>100:
#        b.append(item)
# print(b)


#Shorthand

b=[i for i  in list if i>100]
print(b)

#Set 
a = [1,2,3,4,5,5,5,3,2,1]
b = {i for i in a} #no repeated values
print(b)