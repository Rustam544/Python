import functools


def type_logger(func):
    @functools.wraps(func)
    def tag_wrapper(*args, **kwargs):
        for i in args:
            print(f'{func.__name__} ( {i} : {type(i)} )')
        for i in kwargs:
            print(f'{func.__name__} ( {kwargs[i]} : {type(kwargs[i])} )')
        markup = func(*args, **kwargs)
        return markup

    return tag_wrapper


@type_logger
def calc_cube(*args, **kwargs):
    """Return cube numbers"""
    for i in args:
        yield i ** 3
    for i in kwargs:
        yield kwargs[i] ** 3


a = calc_cube(5, 4, 5.3, s=15, q=54)
for i in a:
    print(i)