""" 
DRY PRINCIPAL 
Do Not Repeat Yourself 
"""
# ***********************************
""" 
PascalCase
EmployeeName --->PascalCase

camelCase
isNumeric, isFloatOrInt ---->camelCase 
"""


class Number:
    def sum(self):
        return self.a+self.b

num=Number()

# num.a =int(input())
# num.b=int(input())

num.a =12
num.b=123
s=num.sum()
print(s)