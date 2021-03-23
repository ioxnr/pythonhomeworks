def val_checker(predicate):
    def assert_predicate(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not predicate(result):
                raise ValueError(f'result {result!r} does not satisfy the predicate')
            return result

        return wrapper

    return assert_predicate


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
a = calc_cube(-5)
print(a)
