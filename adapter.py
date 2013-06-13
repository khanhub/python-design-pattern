#!/usr/bin/env python
class Player(object):
    def __init__(self, name):
        self.name = name or ''

    def Attack(self, name):
        raise NotImplementedError("must be subclass")

    def Defence(self, name):
        raise NotImplementedError("must be subclass")

class Forwards(Player):
    def Attack(self):
        print "Forwards: ", self.name, " Attack!"

    def Defence(self):
        print "Forwards: ", self.name, " Defence!"

class Backwards(Player):
    def Attack(self):
        print "Backwards:", self.name, "Attack"

    def Defence(self):
        print "Backwards: ", self.name, " Defence!"

class ForeignMiddle(object):
    def __init__(self, name):
        self.name = name or ''

    def ForeignAttack(self):
        print "ForeignMiddle:", self.name, "ForeignAttack"

    def ForeignDefence(self):
        print "ForeignMiddle: ", self.name, " ForeignAttack!"

class Adapter(Player):
    def __init__(self, name):
        self.foreignMiddle = ForeignMiddle(name)

    def Attack(self):
        self.foreignMiddle.ForeignAttack()

    def Defence(self):
        self.foreignMiddle.ForeignDefence()

if __name__ == '__main__':
    forwards = Forwards("lcy")
    forwards.Attack()
    forwards.Defence()
    
    adapter = Adapter("lxx")
    adapter.Attack()
    adapter.Defence()