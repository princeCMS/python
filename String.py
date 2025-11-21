# string in python are surrounded by either single quotation marks or double and u can print string in print() function
print('hi, todays friday')
print("hi, tomorrow i go home")

# assign string to a variable
a = "hello"
print(a,type(a))


# Python doesnt have a char dataType means 'p' consider as a string
name ="Prince"
print(name[0],type(name))

# and yes string are array means u can loop through in it
name= "Singla"
for i in name:
    print(i)

# print the length of a string
print(len(name))

# to check if certain char present in a string or not and it give output in boolean  by 'in keyword'
txt = "So tomorrow i go home and return on monday"
print("tomorrow" in txt)

txt2= "Hi, todays date is 21"
print("21" in txt2)

# Slicing: to return a part of a string, we can use slice syntax
# i: get the character from position 2 to 5(not including)
txt3 = "This is the end... hold ur breadth and count to 10"
print(txt3[3:6])

# Modify String: Python has in-built method which return the modifying string

# i: upper case()
name = "Prince"
print(name.upper())
# lets check is this change in my original or not
print(name,name==name.upper())

# same for lower

# ii: replace(): replace method(): replace a string to another string : it return not change in original
state = "Haryana"
state.replace("Haryana","Punjab")
print(state)

# iii: Concat two string

a = "Hello"
b = "world"
c = a+" "+b
print(a,b,c)

# imp: we cant write like this print("Hii todays date is"+21) cant concat string and number

# iv: escape character(\): its main task is print whatever u write after \