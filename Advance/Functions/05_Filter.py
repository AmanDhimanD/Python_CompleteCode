# def fun(num):
#     if num>5:
#         return True
#     else:
#         return False

fun=lambda x: x>5
l=[1,2,3,4,45,35,43,523]

print(list(filter(fun,l)))