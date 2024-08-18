
# import module2 as m2
# from module2 import a,b, say_hi # также после импорта можно поставить * - означает импортировать всё
# from module2 import *
# print(dir(module2))
from modules.module2 import say_hi as sh
import sys

sh()
print("Привет я из модуля 1")
b = 10
for path in sys.path:
    print(path)
# print(module2.a)
# say_hi()
# print(a)
# print(b)
