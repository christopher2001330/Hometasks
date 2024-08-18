# namespaces
import math
from modules.module3 import d

# def square(x):
#     return "Ok"
d = 7
def square(x):
    # global d
    # a = x ** 2
    # print(locals())
    # return a
    # global d
    # d = d ** 2
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        # d = x * 2
        if d % 2 == 0:
            print("Чётное")
        else:
            print("Нечётное")

    even(x)
    return d

a = 5
# print(f'{math.sqrt(a):.2f}')
b = square(4)
print(a)
print(b)
print(globals())
