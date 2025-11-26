# Python has four main collection dataType 1. List 2. Tuple 3. Set 4. Dictionary

# 4️⃣ Dictionary

# Key–value pairs
# Ordered (Python 3.7+)
# Mutable
# Example:
# {
#   "name": "Prince", 
#   "age": 20
# }


dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
print(dic)
print(dic["name"])
print(dic["address"]["pincode"])

# Here we write which thing is similar like previous collection
# to get length is same, get type also same, check key present or not, 

dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
print(type(dic["name"]))


# keys(): return the all keys as list form but remember this is not a normal list
# if u add any key in future then that list can sniff it
# same happened with values()
dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
print(type(dic.keys()))
for x in dic.keys():
    print(x)

valueData =  dic.values()
print(valueData)
dic["address"]["pincode"]=121103
print(valueData)
print(dic["address"]["pincode"])

# Remove items from dict
dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
print(dic.pop("age")) # return the value
print(dic)

# Looping a dic return the key from that dic variable
dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
for x in dic:
    print("Keys: ",x,"| value: ",dic[x])

# copy() a dict that doesn't change in original dict
dic = {
    "name": "Prince",
    "age": 20,
    "address": {
        "pincode": 121106
    }
}
temp1 = dic.copy()
temp1["name"]="Prince Singla"
print(dic)

temp2 = dic
temp2["name"]='Prince Singla'
print(dic)