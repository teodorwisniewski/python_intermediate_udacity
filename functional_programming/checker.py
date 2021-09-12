import inspect
import functools


def bind_args(function, *args, **kwargs):
    return inspect.signature(function).bind(*args, **kwargs).arguments


def check_types(severity=1):
    def checker(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if severity == 0:
                return function(*args, **kwargs)
            parameters = bind_args(function, *args, **kwargs)
            message = ""
            for param, value in parameters.items():
                param_type = function.__annotations__[param]
                if not isinstance(value, param_type):
                    message = message + f"Parameter {param} is not {param_type} datatype.  \n" \
                                        f"The following value and type has been supplied: {value}:{repr(type(value))}\n\n"
            if message and severity==1:
                print(message)
            if message and severity==2:
                raise  TypeError(message)
            return function(*args, **kwargs)
        return wrapper
    return checker


decorator = check_types()
@decorator
def compute(a: int, name: str, sep:str =" ") -> str:
    l = [name]*a
    return sep.join(l)


decorator = check_types(severity=2)
@decorator
def compute2(a: int, name: str, sep:str =" ") -> str:
    l = [name]*a
    return sep.join(l)


if __name__ =="__main__":
    print(compute2(3, "John",sep="<---->"))
    print(compute2([3,2], ("hey",), sep=2))

