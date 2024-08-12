# def print_params(a,b,c):
#     print(a,b,c)
#     print(a+c)
# print_params(2,True,1)
# def print_params(a=1,b=2,c=2):
#     print(a,b,c)
#
# print_params(2,5,c='String') # сначала 2,5 потом строка и никак иначе
# # сколько параметров принимает функция, столько и отдаем
# # * - первращает в именнованый параметр
# def print_params(a=1,*, b=2,c=2):
#     print(a,b,c)
# def func_with_params(a=1, b=2): # параметры по умолчанию, также если один из них с равно, то он должен быть последним
#     print(a + b)
#
#
#
# func_with_params(3,3)
# func_with_params ()
# func_with_params()
def func_with_params(a, b=2, c = None):
    if c is None:
        c=[]
        c.append(a)
        print(c) # модуль добавлен чтобы не добалялся в текущий список снова и снова

func_with_params(3)
func_with_params(3)
func_with_params(3)
func_with_params(4) # каждый вызов добавляет в сущсетвующий список параметр