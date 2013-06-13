#!/usr/bin/env python
class Interface(object):
    def flowers(self):
        raise NotImplementedError("must subclass")

    def water(self):
        raise NotImplementedError("must subclass")

    def money(self):
        raise NotImplementedError("must subclass")

class SchoolGirl(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Pursuit(Interface):
    def __init__(self, name):
        self.mm = name

    def flowers(self):
        print "send flowers to: ", self.mm

    def water(self):
        print "send water to: ", self.mm

    def money(self):
        print "send money to:", self.mm

class Proxy(Interface):
    def __init__(self, name):
        self.pursuit = Pursuit(name)

    def flowers(self):
        self.pursuit.flowers()

    def water(self):
        self.pursuit.water()

    def money(self):
        self.pursuit.money()

if __name__ == '__main__':
    girl = SchoolGirl("lxx")
    proxy = Proxy(girl.getName())
    proxy.flowers()
    proxy.water()
    proxy.money()