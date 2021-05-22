story='''This is short story of PY.
         this is unable now'''
print(len(story))

a="rayne"
#upper function
print(a.upper())

b=" RAYNE"
#lower function
print(b.lower())

#remove whitespace
print(b.strip())

#Replace
print(a.upper().replace("e", "er"))

#Concatenation 
x="My age is {}"
y=20
print(x.format(y))

print("Coder Age is {}.".format(y))
#also by this 
print(f"Coder age is {y}.")
