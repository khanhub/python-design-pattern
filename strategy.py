#!/usr/bin/env python
class Strategy(object):
    def algorithmInterface():
        raise NotImplementedError("Must subclass me")

class ConcreteStrategyA(Strategy):
    
    def algorithmInterface(self):
        print 'algorithmInterface A'

class ConcreteStrategyB(Strategy):
    
    def algorithmInterface(self):
        print 'algorithmInterface B'

class ConcreteStrategyC(Strategy):
    
    def algorithmInterface(self):
        print 'algorithmInterface C'

class Context(object):
    def __init__(self, strategy):
        self._strategy = strategy

    def run(self):
        self._strategy.algorithmInterface()


class Client(object):
    @staticmethod
    def main():
        strategy = ConcreteStrategyA()
        context = Context(strategy)
        context.run()

        strategy = ConcreteStrategyB()
        context = Context(strategy)
        context.run()

        strategy = ConcreteStrategyC()
        context = Context(strategy)
        context.run()

Client.main()