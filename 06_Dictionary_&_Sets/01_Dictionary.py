""" Dictionaries are used to store data values in key:value pairs.
It is unordered
It is mutable,indexed,Cannot contain duplicate keys """

# "name": "identity" in this,
# name is key and identity is value pair
dict = {
    "name": "identity",
    "email": "gmail,yahoo!!",
    "Id": "integers",
    "color": "red"
}
print(dict)
print(dict["Id"])

print("\nBY LOOP")
for i in dict:
    print(i)
