import inspect
import functools


def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments


def check_types(severity=1):
    if severity == 0:
        return lambda function: function

    def message(msg):
        if severity == 1:
            print(msg)
        else:
            raise TypeError(msg)
    def checker(function):
        expected = function.__annotations__

        assert(all(map(lambda exp: isinstance(exp, type), expected.values())))
        if not expected:
            return function
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            bound_arguments = bind_args(function, *args, **kwargs)
            for arg, val in bound_arguments.items():
                if arg not in expected:
                    continue
                if not isinstance(val, expected[arg]):
                    message(f"Bad Argument! Received {arg}={val}, expecting object of type {expected[arg]}")
            retval = function(*args, **kwargs)
            if 'return' in expected and not isinstance(retval, expected['return']):
                message(f"Bad Return Value! Received {retval}, but expected value of type {expected['return']}")
            return retval
        return wrapper
    return checker


@check_types(severity=2)
def foo(a: int, b: str) -> bool:
    res = b[a] == 'X'
    if len(b)>4:
        res = None
    return res


if __name__ == "__main__":
    # When used correctly, everything is great!
    print(foo(3, 'ABCD'))  # => False
    print(foo(1, 'WXYZ'))# => TRUE

    # But if the arguments are the wrong type, this decorator function will severely complain!

    # Lots of information about an error
    # TypeError: Bad Argument! Received a=WXYZ, expecting object of type <class 'int'>
    #
    # Note that, since this is a function that produces decorators, even if we wanted to decorate it
    # with the default severity we'd need to call our function:

    @check_types(severity=2)
    def funkcja(a,b,c=2):
        return a+b*c

    print(funkcja("John", "Sally",c=5))


    @check_types(severity=2)
    def funkcja2(a:1,b,c=2):
        return a+b*c

    print(funkcja2("John", "Sally",c=5))

    print(foo(1, 'WXYZdwfewa'))
    @check_types()  # <-- The function is still invoked.
    def foo(a: int, b: str) -> bool:
        return b[a] == 'X'

    # This isn't strictly necessary, but if we want to decorate callables with just check_types
    # then we'd have to modify the implementation.
    # ;