

def echo(arg):
    return arg

print(echo)
print(id(echo))
print(echo(100))
print(hex(id(echo)))
foo = echo
print(foo)
print(id(foo))
print(hex(id(foo)))

print(locals())

print('echo' in locals())
print(globals())
print(globals()==locals())


def fun1(arg):
    """
    This funtion connects user to the db
    :param arg:
    :return:
    """

print(help(fun1))
