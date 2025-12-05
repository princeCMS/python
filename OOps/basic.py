import uuid
# creating student records using oop's

# class:- blueprint or template
# object: instance of class
# object only store variable not constructor , getter() setter(), any types of function

# 1st.
# class Student:
#     pass

# student1 = Student()
# print(student1,id(student1),hex(id(student1)))


# 2nd.
# class UserAccount:
#     accNumber = uuid.uuid4().hex
#     accName = "Prince"

# prince = UserAccount()
# samreen = UserAccount()
# print(prince.accNumber,prince.accName)
# print(samreen.accNumber,samreen.accName)

# 3rd.
class UserAccount:
    # accName = None
    
    def __init__(self,accNumber1,accName1):  # this is a constructor
        self.accNumber = accNumber1
        self.accName = accName1

user1 = UserAccount(uuid.uuid4().hex,'Prince')
user2 = UserAccount(uuid.uuid4().hex,'Samreen')
# user3 = UserAccount()

print(user1.accNumber,user1.accName)
print(user2.accNumber,user2.accName)
# print(UserAccount.accName)


# 4th.
class Student:
    rollNo = None
    name = None

    # setter()
    def setRollNo(self,rollNo):
        self.rollNo = rollNo

    def setName(self,name):
        self.name = name

    # getter()
    def getRollNo(self):
        return self.rollNo
    
    def getName(self):
        return self.name
    
student1 = Student()
student1.setRollNo(2210992088)
student1.setName('Prince')

student2 = Student()
student2.setRollNo(2210992240)
student2.setName("Samreen")

print(student1.getRollNo(),student1.getName())
print(student2.getRollNo(),student2.getName())


class Employee:
    def __init__(self,empId,empName,empGender,empSalary): # constructor
        self.empId = empId
        self.empName = empName
        self.empGender = empGender
        self.empSalary = empSalary

    # setter and getter
    def setEmpId(self,empId):
        self.empId = empId

    def getEmpId(self):
        return self.empId
    
    def setEmpName(self,empName):
        self.empName = empName

    def getEmpName(self):
        return self.empName
    
    def setEmpGender(self,empGender):
        self.empGender = empGender

    def getEmpGender(self):
        return self.empGender
    
    def setEmpSalary(self,empSalary):
        self.empSalary = empSalary

    def getEmpSalary(self):
        return self.empSalary

emp1 = Employee(779,'Prince','Male',200)
emp2 = Employee(874,'xyz','Female',847)

emp1.setEmpId(2088)
emp1.setEmpName('Prince Singla')
emp1.setEmpSalary(150)
print(emp1.getEmpId(),emp1.getEmpName(),emp1.getEmpGender(),emp1.getEmpSalary())

