import inspect
import functools


def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments


def check_types(severity=1):
    def checker(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            # Do something neat!
            return function(*args, **kwargs)
        return wrapper
    return checker


@check_types(severity=2)
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'


if __name__ == "__main__":
    # When used correctly, everything is great!
    print(foo(3, 'ABCDE'))  # => False
    print(foo(1, 'WXYZ'))  # => TRUE

    # But if the arguments are the wrong type, this decorator function will severely complain!
    print(foo('WXYZ', 1))


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
    print(foo(1, 'WXYZ'))  # => TRUE

    # But if the arguments are the wrong type, this decorator function will severely complain!
    print(foo('WXYZ', 1))