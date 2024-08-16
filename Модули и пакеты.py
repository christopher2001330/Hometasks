
# import module2 as m2
# from module2 import a,b, say_hi # также после импорта можно поставить * - означает импортировать всё
# from module2 import *
# print(dir(module2))
import module2 as m2
print("Привет я из модуля 1")

# print(module2.a)
# say_hi()
# print(a)
# print(b)
print(m2.__name__)