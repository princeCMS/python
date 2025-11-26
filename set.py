# Python has four main collection dataType 1. List 2. Tuple 3. Set 4. Dictionary
# 3️⃣ Set

# Unordered
# No duplicates
# Cannot access by index
# Sets are written with curly brackets.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Example:
# {1, 2, 3}


# ✅ Sets ARE mutable
# You can:

# add elements
# remove elements
# update the set not their elements
# So the set itself can change.
# set store immutable objects
# ❌ Set items ARE unchangeable

# This means:
# 👉 You CANNOT modify an individual element of a set.

set1 = {1,2,8,"Prince",1}
print(set1)

# set mostly similar like list and tuple here we write
# Get length(), get a type of set, 


# we cant get element by index but get by looping through
set1 = {1,2,8,"Prince",1}
for value in set1:
    print(value)

# check if item present in set or not
set1 = {1,2,8,"Prince",1}
name="Prince"
if(name in set1):
    print(name+" present in set")
else: print(name+" not present in set")

# add() items in sets
set1 = {1,2,8,"Prince",1}
set1.add("Singla")
print(set1)

# add() items of another set to current set then use update() method
set1 = {1,2,8,"Prince",1}
temp = {1,8,7,"Singla",5}
set1.update(temp)
print(set1,type(set1))
# and temp can be any collection like: list,set,tuple,dic

# Remove items from sets
set1 = {1,2,8,"Prince",1}
print(set1.remove(1))
print(set1)


# pop() method remove random item from set and it return that item
set1 = {1,2,8,"Prince",1}
print(set1.pop(),set1.pop())
print(set1)

# clear(): clear all the data from set or empty the set
set1 = {1,2,8,"Prince",1}
print(set1.clear())
print(set1)

