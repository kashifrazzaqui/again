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


