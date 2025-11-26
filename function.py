# in python function defined as a 'def' keyword following by function name and parenthesis 
def my_function():
    print("This is my first function")
my_function()

# function send the data back to who call them using the return statement
def sum(first,second):
    return first+second
print(sum(2,3))


def checkType(data):
    if(type(data) in [list,set,dict]): return "Mutable"
    else: 
        print(type(data))
        return "Immutable"
print(checkType(()))

