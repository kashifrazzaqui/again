again
=======
Python utilities for stuff you have to do again and again...
Python decorators for type and value checking at runtime. Also, some boilerplate code for making classes that support event registration and firing.


### logging decorators

Logs parameters provided and result returned. it comes in two forms _@log_ and _@logx_

*@log* takes no arguments, prints params and result

*@logx*

Takes four optional arguments both are boolean and False by default
 - *supress_all_args* takes a boolean and suppresses all args
 - *supress_args* takes a list of string arg names to supress
 - *supress_results* takes a boolean
 - *reciever* takes a function for logging which takes a string as a parameter, by default receiver
   is set to None which causes it to print string to stdout


``` python

@log
def my_func(name, gender):
    age = findByGender(name)
    return age
```

``` python

@logx(supress_results=True)
def my_func(name, gender):
    age = findByGender(name)
    return age
```


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
        # parameters for fire are 'event name' followed by anything you want to pass to the listener
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
