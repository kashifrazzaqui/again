__author__ = 'kashif'
import sys
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

def log(fn):
    def func(*args, **kwargs):
        print (RED + BOLD + '>> ' + END + 'Calling {0} with args {1} and kwargs {2}'.format(fn.func_name, args, kwargs))
        result = fn(*args, **kwargs)
        print (BLUE + BOLD + '<< ' + END + 'Return {0} with result :{1}'.format(fn.func_name, result))
        return result
    return func


def value_check(arg_name, pos, allowed_values):
    """
    allows value checking at runtime for args or kwargs
    """
    def decorator(fn):

        #brevity compromised in favour of readability
        def logic(*args, **kwargs):
            arg_count = len(args)
            if arg_count:
                if pos < arg_count:
                    if args[pos] in allowed_values:
                        return fn(*args, **kwargs)
                    else:
                        raise ValueError("'{0}' at position {1} not in allowed values {2}".format(args[pos], pos, allowed_values))
                else:
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        if value in allowed_values:
                            return fn(*args, **kwargs)
                        else:
                            raise ValueError("'{0}' is not an allowed kwarg".format(arg_name))
                    else:
                        #partially applied functions because of incomplete args, let python handle this
                        return fn(*args, **kwargs)
            else:
                if arg_name in kwargs:
                    value = kwargs[arg_name]
                    if value in allowed_values:
                        return fn(*args, **kwargs)
                else:
                    raise ValueError("'{0}' is not an allowed kwarg".format(arg_name))
        return logic
    return decorator

def type_check(arg_name, pos, reqd_type):
    """
    allows type checking at runtime for args or kwargs
    """
    def decorator(fn):

        #brevity compromised in favour of readability
        def logic(*args, **kwargs):
            arg_count = len(args)
            if arg_count:
                if pos < arg_count:
                    if isinstance(args[pos],reqd_type):
                        return fn(*args, **kwargs)
                    else:
                        raise TypeError("'{0}' at position {1} not of type {2}".format(args[pos], pos, reqd_type))
                else:
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        if isinstance(value, reqd_type):
                            return fn(*args, **kwargs)
                        else:
                            raise TypeError("'{0}' is not of type {1}".format(arg_name, reqd_type))
                    else:
                        #partially applied functions because of incomplete args, let python handle this
                        return fn(*args, **kwargs)
            else:
                if arg_name in kwargs:
                    value = kwargs[arg_name]
                    if isinstance(value, reqd_type):
                        return fn(*args, **kwargs)
                else:
                    raise TypeError("'{0}' is not of type {1}".format(arg_name, reqd_type))
        return logic
    return decorator

