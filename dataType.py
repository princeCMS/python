import random
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# getting the datatype of a variable
name = "Prince"
print(type(name))

# Setting the Specific Data Type

strNum = "20"
number= int(strNum)
print(type(strNum),type(number))

# let's talk about random number 
num= random.randrange(1,15)
if num in [7 , 8 , 9]:
    print("You'r an imposter",num)
else: print("You'r crewmate",num)