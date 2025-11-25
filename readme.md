# 1st:
✅ Assignment and modification are different operations.
✔ Modification (mutation)

Changes the inside of an existing object.
Allowed only for mutable objects (like list, dict, set).

✔ Assignment

Makes the variable point to a new object.
Happens for all objects (mutable or immutable).

# 2nd:
✅ Final Clear Rule
**In Python, EVERYTHING is an object.
Every object is created from some class — whether it's mutable or immutable.**

5 → object
created from class int (immutable)

"hello" → object
created from class str (immutable)

[1,2,3] → object
created from class list (mutable)

{"a": 1} → object
created from class dict (mutable)


# 3. we have some list methods()
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list