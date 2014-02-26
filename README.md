pyutils
=======

Python decorators for type and value checking at runtime. Also, some boilerplate code for making classes that support event registration and firing.


### Value checking decorator

Takes three arguments (var_name_of_parameter, position_in_parameters, allowed_values) and throws a
ValueError if the value in the specified parameter is not present in the allowed_values.

* var_name_of_parameter - is just the variable name
* position_in_parameters - is the index at which this parameter is in the function definition. The
* first argument passed to a function is '0' and the second one is '1' and so on.
allowed_vals - is a list of allowed values that this variable can hold.

``` python
allowed_vals = ["a", "b", "c", "d"]

@value_check("second", 1, allowed_vals)
def test_value(first, second):
    return first + second
```

### Type checking decorator

Takes three arguments (var_name_of_parameter, position_in_parameters, required_type) and throws a
TypeError if the value in the specified parameter is not of the required_type.

* var_name_of_parameter - is just the variable name
* position_in_parameters - is the index at which this parameter is in the function definition. The
first argument passed to a function is '0' and the second one is '1' and so on.
* required_type - is a Type such as int, string, or your CustomClass.

``` python
@type_check("first", 0, int)
@type_check("second", 1, int)
def test_type(first, second):
    return first + second
```


### Eventing Boilerplate

Defines an EventSource class, which gives its inherting class(its child) the following abilities:
* add/remove listeners to custom events
* listeners can have any signature
* fire listeners for any custom defined event


``` python
from events import *

def simple_listener(payload):
    print("Payload: {0}".format(payload))

class TestClass(EventSource):
    def __init__(self):
        super(TestClass, self).__init__()
        print("ready")

    def event_occurs(self):
        self.fire("big bang event", "what a blast!")


def demo():
    t = TestClass()
    
    # takes an event (any valid python object) and a listener (any valid python function)
    t.add_listener("big bang event", simple_listener)
    
    t.event_occurs() #when the event is fired in this method, the listener is informed

if __name__ == '__main__':
    demo()
```

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/97a1b438eb600bbda17998a7a3195b9a "githalytics.com")](http://githalytics.com/kashifrazzaqui/pyutils)
