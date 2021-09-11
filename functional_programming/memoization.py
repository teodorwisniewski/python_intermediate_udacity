import functools


def memoize(fun):
    fun._cache = {}
    @functools.wraps(fun)
    def modified_fun(*args, **kwargs):
        key = (*args, tuple(kwargs.items()))
        res = fun._cache.get(key,None)
        if res is None:
            res = fun(*args, **kwargs)
            fun._cache[key] = res
            return res
        else:
            return res

    return modified_fun



# def memoize(function):
#     @functools.wraps(function)
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs)
#     return wrapper


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
