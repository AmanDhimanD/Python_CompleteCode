""" 
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression. 
"""
#add 
x = lambda a : a + 10
print(x(5))
#multiple
x = lambda a, b : a * b
print(x(5, 6))
#add three numbers
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))