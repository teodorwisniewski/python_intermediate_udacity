import inspect
import functools


def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments


def check_types(severity=1):
    if severity == 0:
        return lambda fun:fun

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)

    def checker(function):
        expected = function.__annotations__

        if not expected:
            return function
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            provided_args = bind_args(function, *args, **kwargs)
            # assert all(map(lambda el:isinstance(el)))
            for arg,value in provided_args.items():
                if not isinstance(value,expected[arg]):
                    message(f"The function {function.__name__} expected to obtain {arg} of datatype {expected[arg]}"
                            f", but the user provided {arg}={value} of type {type(value)}")
            res = function(*args, **kwargs)
            if "return" in expected and not isinstance(res,expected["return"]):
                message(f"The function {function.__name__} expected to return datatype {expected['return']}"
                        f", but the function returned {res}:{type(res)}")
            return res
        return wrapper
    return checker


@check_types(severity=1)
def foo(a: int, b: str) -> bool:
    res = b[a] == 'X'
    if len(b)>4:
        res = None
    return res


if __name__ == "__main__":
    # When used correctly, everything is great!
    print(foo(3, 'ABCD'))  # => False
    print(foo(1, 'WXYZ'))# => TRUE
    print(foo(1, ['WXYZ',2,3]))  # => TRUE
    # But if the arguments are the wrong type, this decorator function will severely complain!
    print(foo(1,'WXYZdwfewa'))

    # Lots of information about an error
    # TypeError: Bad Argument! Received a=WXYZ, expecting object of type <class 'int'>
    #
    # Note that, since this is a function that produces decorators, even if we wanted to decorate it
    # with the default severity we'd need to call our function:

    @check_types()  # <-- The function is still invoked.
    def foo(a: int, b: str) -> bool:
        return b[a] == 'X'

    # This isn't strictly necessary, but if we want to decorate callables with just check_types
    # then we'd have to modify the implementation.
    # ;

    # When used correctly, everything is great!
    print(foo(3, 'ABCDE'))  # => False
    print(foo(1, 'WXYZ'))# => TRUE

    # But if the arguments are the wrong type, this decorator function will severely complain!

    print(foo('WXYZdwfewa', 1))