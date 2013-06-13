#!/usr/bin/env python
class Operation(object):
    def __init__(self):
        self.numA = 0
        self.numB = 0

    def setNumA(self, value):
        self.numA = value
    
    def setNumB(self, value):
        self.numB = value

    def getRes(self):
        raise NotImplementedError("must be subclass")

class OperationPlus(Operation):
    def getRes(self):
        return self.numB + self.numA

class OperationSub(Operation):
    def getRes(self):
        return self.numB - self.numA

class OperationMul(Operation):
    def getRes(self):
        return self.numB * self.numA

class OperationMod(Operation):
    def getRes(self):
        if self.numB == 0:
            raise ZeroDivisionError("numB can not equal 0")
        return self.numA / self.numB

class OperationFactory(object):
    def createFactory(self, oper):
        self.Operations = {
            "+": OperationPlus(),
            "-": OperationSub(),
            "*": OperationMul(),
            "/": OperationMod()
        }
        return self.Operations[oper]

if __name__ == '__main__':
    factory = OperationFactory()
    oper = factory.createFactory("/")
    oper.setNumB(0)
    oper.setNumA(1)
    print oper.getRes()