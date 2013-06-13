#!/usr/bin/env python
class AbstractSubject(object):
    def register(self, listener):
        raise NotImplementedError("Must subclass me")

    def unregister(self, listener):
        raise NotImplementedError("Must subclass me")

    def notify_listeners(self, event):
        raise NotImplementedError("Must subclass me")

class Subject(AbstractSubject):
    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notice(event)

    def getUserAction(self):
        event = raw_input("input your event:")
        return event

class Listener(object):
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notice(self, event):
        print self.name + " received " + event


if __name__ == '__main__':
    subject = Subject()

    listenerA = Listener("lcy", subject)
    listenerB = Listener("lxx", subject)
    subject.notify_listeners("news")

    action = subject.getUserAction()
    subject.notify_listeners(action)
