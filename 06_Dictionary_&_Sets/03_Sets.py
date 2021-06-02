# set list is unordered, meaning: the items will appear in a random order.
set = {"a", "b", "c"}
print(set)  # Random all time

# Duplicates Not allowed
set = {"a", "b", "c", "a"}
print(set)

# METHODS OF SETS

# add
set.add("d")
print(set)

# update
NewSet = {"e", "f"}
set.update(NewSet)
print(set)

# remove
set.remove("a")
print(set)

