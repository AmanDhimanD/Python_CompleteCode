list1 = [1,2,6]

list2 = []

# for item in list1:
#     fun=lambda x: x*x
#     list2.append(fun(item))
# print(list2)


'''
MAP Function
'''
fun=lambda x: x*x
# print(map(fun,list1))
print(list(map(fun,list1)))
