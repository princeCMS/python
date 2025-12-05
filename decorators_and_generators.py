# decorator: Its a function that take function as an input and 
# return function after decorate it without change in original.

def decor(func):
    print(hex(id(func)))
    # making nested function 
    def inner():
        func()  # existing functionality
        print("Welcome") # add new functionality
    
    print(hex(id(inner)))
    return inner

def message():
    print("Welcome")
    print("Welcome")


print(type(message))
print(hex(id(message)))
decor(message)



# 2. Example

def decorator(addition):
    def inner():
        try:
            sum = float(addition())
            third = float(input("Enter third number: "))
            return third+sum
        except ValueError:
            return "Enter valid input"
    return inner

@decorator
def addition():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        return first+second
    except ValueError:
        return "Enter valid input"
    
# addition = decorator(addition)
print(addition())


# 3. Multiple decorator

# But this is our modification decorator function that return a another function
def decor1(getName):
    def inner():
        fullName = getName()
        return fullName.upper()
    return inner

def decor2(getName):
    def inner():
        return getName().split()
    return inner
        
# This is our normal function
def getName():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    return firstName+' '+lastName

# print(getName())  this function return my full name

# now change the function without changing in capital letter
getName = decor1(getName)
print(getName())

# now after modifying the function i want to modify this moreeee into list
getName = decor2(getName)
print(getName())