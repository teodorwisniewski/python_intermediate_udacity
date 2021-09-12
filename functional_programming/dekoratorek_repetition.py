import functools


def memoize(fun):
    fun._cache = {}
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        key = (*args, tuple(kwargs.items()))
        if key not in fun._cache:
            fun._cache[key] = fun(*args, **kwargs)
        return fun._cache[key]
    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(10))
    print(fib(25))
    print(fib(50))
    print(fib(100))
