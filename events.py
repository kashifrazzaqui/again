class ListenerRegister(object):
    def __init__(self):
        self._register = {}

    def add_listener(self, event, listener):
        event = event.upper()
        listeners = self._register.get(event, set())
        listeners.add(listener)
        self._register[event] = listeners

    def remove_listener(self, event, listener):
        event = event.upper()
        listeners = self._register.get(event, None)
        if listeners:
            listeners.remove(listener)

    def remove_event(self, event):
        event = event.upper()
        del self._register[event]

    def get_listeners(self, event):
        event = event.upper()
        return self._register.get(event, set())

class EventSource(ListenerRegister):

    def __init__(self):
        super(EventSource, self).__init__()

    def fire(self, event, *args, **kwargs):
        for each in self.get_listeners(event):
            each(*args, **kwargs)


class TestClass(EventSource):
    def __init__(self):
        super(TestClass, self).__init__()
        print("ready")

    def event_occurs(self):
        # parameters for fire are 'event name' followed by anything you want to pass to the listener
        self.fire("big bang event", "what a blast!")

    def simple_listener(self, payload):
        print("Payload : {0}".format(payload))


def demo():
    t = TestClass()

    # takes an event (any valid python object) and a listener (any valid python function)
    t.add_listener("big bang event", t.simple_listener)

    t.event_occurs() #when the event is fired in this method, the listener is informed

if __name__ == '__main__':
    demo()
