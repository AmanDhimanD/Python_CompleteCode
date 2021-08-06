def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not corrct.")


x=increment(23)
print(x)
x=increment("23r") #throw error
print(x)