# what is a module in python.
So basically module is a python file contains
i. Function  ii. Variables  iii. Classes  iv. Code u want to reuse

* now we can import that file to another file why? use that code inside it.

* so basically our program import module to use their function in it

example:

* math_tools.py                  -> So this is module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

* another file

import math_tools

print(math_tools.add(3, 5))
print(math_tools.multiply(4, 6))


🟦 Why use Modules?
✔ Reuse code
✔ Organize code
✔ Avoid repeating functions
✔ Make your program cleaner
✔ Share functionality easily

🟦 Python has built-in modules too

Examples:

import math
import random
import os
import datetime


You can use their functions:

import math
print(math.sqrt(25))   

# so basically module is nothing its just use for reusability and we can write like normal 
# python file except taking user input vagera