# Python has four main collection dataType 1. List 2. Tuple 3. Set 4. Dictionary
# 2️⃣ Tuple

# Ordered
# NOT changeable (immutable)
# Allows duplicates
# for tuple use () bracket
# Example:

# (1, 2, 3)

# And yes every collection mostly similar like list if their is any diff we write here
# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# get length(), range of index, check item is present or not, loops are same like list
# if u want to change in tuple so first convert it into list then change and then convert back