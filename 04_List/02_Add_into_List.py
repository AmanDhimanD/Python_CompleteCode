list=["rayne","coder","python","c","c++","java"]
print(list)

list.append("newElement")
print(list)

#add elements by index
list.insert(1,"ByIndex")
print(list)

#extend 
newList1=["a","1","i"]
newList2=["b","2","ii"]

newList1.extend(newList2)
print(newList1)