""" 
The best way to open and close the file automatically is the with(type)
"""
with open('with.text','r') as f:
    a=f.read()

# with open('with.text','w') as f:
with open('with.text','a') as f:
    a=f.write('\nthis is write')
print(a)


