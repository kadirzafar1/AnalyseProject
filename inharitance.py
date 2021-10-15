#from practice import calculator
from pythonTesting.practice import calculator


class childimp1(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self, 2, 3)


    def getdatacompleted(self):
        return self.num2*self.num*self.multiplication()

obj = childimp1()
obj.getdatacompleted()
print(obj.getdatacompleted())


