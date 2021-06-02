# item()
# 	Returns a list containing a tuple for each key value pair
dict = {
    "name": "identity",
    "email": "gmail",
    "Id": "integers",
    "color": "red"
}
y = dict.items()
print(y)

# keys()
y = dict.keys()
print(f"\n\n{y}")

# update()
dict.update({"color": "White"})
print(f"\n\n{dict}")

# The get() method returns the value of the item with the specified key.
x=dict.get("name")
print(x)
