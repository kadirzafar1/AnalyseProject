class calculator():
    num = 100
    def getData(self):
        print("i am executing as method in class ")


obj = calculator()  # syntax of object creation
obj.getData()
print(obj.num)

print("***********First Index******")

# Case no-2, How to use constructor

class calculator():
    num = 100

    #default constructor

    def __init__(self):
        print("i am called automatically when object is created")

    def getdata(self):
        print(" i am now executing as method in class")

obj = calculator()
obj.getdata()
print(obj.num)


print("******* Second Index *****")

# Case No-[3, parametrise, use of constructor,mthod class variable and instance variable

class calculator():
    num = 100

    def __init__(self,a,b):
        self.firstnumber = a    #instance variable
        self.secondnumber = b   #instance variable
        print(" i am called automatically when object is created")

    def getdata(self):
        print(" i am now executing as method in class")

    def multiplication(self):
        return self.firstnumber*self.secondnumber*calculator.num

obj = calculator(2, 3)
obj.getdata()
print(obj.multiplication())


obj1 = calculator(4, 5)
obj1.getdata()
print(obj1.multiplication())



