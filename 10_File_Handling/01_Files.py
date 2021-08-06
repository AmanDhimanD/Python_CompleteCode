f=open('This.txt','r')
# this is Default read mode of file
f=open('This.txt') #open file

# data=f.read()
data=f.read(5) #Starting 5 characters from file

print(data) 
f.close() 