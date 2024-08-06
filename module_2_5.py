# def say_hello(name):
#     print("Hello", name) #функцию можно вызывть много раз

# say_hello("Denis")
# say_hello("Max")

# import random
# def lottery():
#     tickets = [1,2,3,4,5,6,7,8,9,10]
#     win = random.choice(tickets)
#     return win

# win = lottery() + lottery()
# print(win)
# import random
#
#
# def lottery(*args, **kwards): #args - именной параметр
#     tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     win1 = random.choice(tickets)
#     tickets.remove(win1)
#     win2 = random.choice(tickets)
#     print(*args)
#     return win1, win2
#
# win1, win2 = lottery(1,2,3)
# print(win1, win2)
def test(a=2,b=True):
    print(a,b)

# test(False, "ok")# переназначаем парамтеры
test(*[1,2])# список встал на место параметра номер один * распаковка списка

