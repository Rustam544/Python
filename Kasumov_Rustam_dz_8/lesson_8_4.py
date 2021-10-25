def val_checker(lambda_z):
    def tag_wrapper(func):
        def func_val(args):
            if lambda_z(args):
                markup = func(args)
            else:
                msg = f'wrong val {args}'
                raise ValueError(msg)
            return markup

        return func_val

    return tag_wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Return cube numbers"""
    return x ** 3


print(calc_cube(3))
