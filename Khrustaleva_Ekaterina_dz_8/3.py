def type_logger(func):
    def wrapper(arg):
        result = func(arg)
        print(f'{func.__name__}({arg}: {type(arg)})')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
