# def var_checker(verbosity=2):
#     def _logger(func):
#         def wrapper(*args):
#             result = func(*args)
#             msg = f'\tcall {func.__name__}'
#             if verbosity > 0:
#                 msg = f'{msg}({", ".join(map(str, args))})'
#             if verbosity > 1:
#                 msg = f'{msg} -> {result}'
#             return msg
#
#         return wrapper
#
#     return _logger
#
#
# @var_checker()
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# password_f = render_input('password')
# print(username_f)
# print(password_f)

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p

r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())