
#!/usr/bin/env python
class Person(object):
    def __init__(self, name):
        self.name = name or ""
    
    def Show(self):
        print "decotate: ", self.name

class Finery(Person):
    def Decorate(self, component):
        self.component = component

    def Show(self):
        self.component.Show()

class Tshirt(Finery):
    def __init__(self):
        return

    def Show(self):
        print "Tshirt"
        self.component.Show()

class BigTrouser(Finery):
    def __init__(self):
        return
        
    def Show(self):
        print "BigTrouser"
        self.component.Show()

class UI():
    tx = Person("lcyang")
    ts = Tshirt()
    bt = BigTrouser()
    ts.Decorate(tx)
    bt.Decorate(ts)
    bt.Show()
