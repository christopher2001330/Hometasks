# int() --> int(input())
# float() --> плавающее число
# bool()
# str()
# list()
# tuple()
# dict()
# set()
# type = 0
# if type:
#     print('ok')
# salary = [2300,1800.801234,5000,1234.583434,7500.12323]
# print(round(sum(salary)/len(salary),2), "средняя зарплата в компании") #round - округление
# print(round(max(salary), 2), "максимальная зарплата в компании")
# print(round(min(salary), 2), "минимальная зарплата в компании")
#
# names =["Денис", "Антон", "Егор", "Катя", "Женя"]
# zipped = dict(zip(names, salary))
# print(zipped["Денис"], "-зарплата Дениса")
#Занятие номер два

a = [1,1,1]
b = ""
d =[1,1,1]
c = d
c [0]=2
print(c)
print(d)
print(a is d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)
print(id(268))
# print(any(a)) #"any достаточно хотя бы однон элемента тру"
# print(all(a))
# #Интроспекция - способность получить информацию об атрибутах и типах
print(dir(b))
# print(type(b))
# print(isinstance(b,str))
# print(type(b)==str)
print(help(print))
def helper():
    """
    Эта функция помощник
    """
    pass
print(helper.__doc__) # вызов строки документирования