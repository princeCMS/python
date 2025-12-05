# so this is a run-time exception so its not a compile time error
# and after error the code stop and rest of code not work and 
# so we need to handle this exception

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))

# ans = first/second
# print(ans)
# print("Hello world")

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# try:
#     ans = first/second
#     print(ans)
# except:
#     print("Zero not divided")

# print("Tu ibteda meri tu inteha meri")




# what if i write my name because its my keyboard

# try:
#     first = int(input("Enter first number: "))
#     second = int(input("Enter second number: "))
#     ans  = first/second
#     print(ans)
# except :
#     print("Error occurred: ",e)

# print("Daulat shohrat kya karni, tere pyar ka sahara kafi hai")




# You write	Meaning
# except ValueError:	Catch wrong value errors
# except ZeroDivisionError:	Catch division errors
# except TypeError:	Catch wrong type errors
# except:	Catch ALL errors (not recommended)
# except Exception as e:	Catch error + show message


try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    size= int(input("Enter the size of list: "))
    lst = [-1]*size
    print(lst[size-1])
    print(first/second)

except ValueError:
    print("You write wrong value which is not supposed")

except TypeError:
    print("You type something Wrong")

except Exception as e:
    print(e)

print("Hii")

