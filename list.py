# Python has four main collection dataType 1. List 2. Tuple 3. Set 4. Dictionary

# List are used to store multiple values in single variable 
# and that values can be any and diff types

list  = [2,5,7]
temp = list
temp[0]="Prince"
print(temp)
print(list)

a = "Prince"
b = a

print("So in Python it will assign as a reference but change happen in mutable")
print(id(a))
print(id(b))

b = "Singla"

print(id(a))
print(id(b))

print(b)
print(a)

print("Let's talk about List")
list1 = [1,2,5]
list2 = list1
print(id(list1))
print(id(list2))

list2[0]="Python"
print(list1,id(list1))
list2=["Prince","Singla"]
print(id(list1))
print(id(list2))

# ✅ Python has 4 main collection data types
# 1️⃣ List

# Ordered
# Changeable (mutable)
# Allows duplicates
# Example:
# [1, 2, 3]

# try to print length of list
list = ["Prince","Singla"]
print(len(list))
print(type(list)) 

a = 5
print(type(a))

# Range of Indexing: return the new list while specifying the range
list = ["Prince","Singla",779,"Python","django"]
print(list[1:3])  # last one not consider

# Check if item is present in list or not
list  = ["Prince","Singla",779,"Python","django"]
print("prince" in list)
print(779 in list)

# append item in list: to insert item at the end of list
# and u know whenever we create list then actually we create an object and their 
# class name is list and and these append(), ... all method is the part of that class

list = ["Prince"]
list.append("Singla")
print(list)
list.append(("779","Python"))
print(type(list[2]))

# insert item to a specific index
fruits = ["Orange","Banana","Mango"]
fruits.insert(2,"Grapes")
print(fruits)
fruits.insert(0,{"fav": ["Mango","watermelon"]})
print(fruits)

# Extend list: to append element from another list to original list
# The extend() method does not have to append only lists but you can add any iterable object (tuples, sets, dictionaries etc.).
fruits = ["Mango","Watermelon"]
veg = ["Tomato","LadyFinger"]
fruits.extend(veg)
print(fruits)
fruits.extend(("banana","Orange"))
print(fruits,type(fruits))

# tuple = ('banana')
# tuple.extend()   this one is wrong

# Remove(): the remove() method removes the specified item not from index
# if u want to remove from index then use pop() method best.

fruits = ['Orange','Banana','Orange']
fruits.remove('Orange') # only first 'Orange' be removed
print(fruits)

fruits = ['Orange','Banana',('first','second'),'Orange']
fruits.remove(('first','second'))
print(fruits)

# pop(): the pop() method remove the specified index if u mentioned otherwise
# remove last elements

empDataId = [{779: "Prince"},{"780":"Singla"},{778: "Tushar"}]
empDataId.pop(0)
print(empDataId)
empDataId.pop()
print(empDataId)

print(empDataId.append({779: "Prince"}))
print(empDataId)

# clear(): its clear the list data
empDataId = [{779: "Prince"},{778: "Tushar"}]
print(empDataId)
print(empDataId.clear())
print(empDataId)

# Loop through a list 
# Here we loop through the list item

fruits = ['banana','mango','grapes']
for x in fruits:
    print(x)

# Here we loop through the index number

fruits = ['banana','mango','grapes','watermelon']

index = [0,1,2,3,4,5]
for x in index:
    if(x!=len(fruits)):
        print(fruits[x])
    else: break


for i in range(len(fruits)):
    print(i)

for i in range(len(fruits)):
    print(fruits[i])

# accessing element from list using while loops
fruits = ["Mango","Banana","WaterMelon"]
i=0
while(i< len(fruits)):
    print(fruits[i])
    i+=1

# Sort(): sort the list in ascending order
fruits = ["Mango","Banana","WaterMelon"]
print(fruits.sort())
print(fruits)

# want to sort in reverse order?
fruits = ["Mango","Banana","WaterMelon"]
fruits.sort(reverse= True)
print(fruits)


# Copy a List but not as a reference
fruits = ["Mango","Banana","WaterMelon"]
temp = fruits.copy()
print("Before copy: ",fruits,"After copy: ",temp)
temp[2]='Sweat Berry'
print("Before copy: ",fruits,"After copy: ",temp)

# Join two list
# 1). using + operator
# 2). By append() using loop
# 3). using extend() function
 