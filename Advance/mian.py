""" from click import argument
from soupsieve import match


def sum(a,b):
    return a+b

def condition(a,b):
    if a>b:
        return a
    elif a==b:
        return "equal"
    else:
        return b

def switchCases(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case default:
            return "NONE"
    

if __name__ = "__main__":
    argument=0
    switchCases(argument)
 """

