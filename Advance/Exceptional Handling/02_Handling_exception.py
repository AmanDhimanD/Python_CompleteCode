from typing import Text


try:
    a=int(input("Enter a number:- "))
    d=1/a
    print(d)

except ValueError as e:
    print("\nDon't enter string or character.....")

except ZeroDivisionError as e:
    print("\nDon't use 0 as divisor.........")
# except TypeError as e:
#     print(e)

