# Максимум в списке
# Подсчёт четных чисел в списке
# уникальный список


# def find_max(list_):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return max_
#
# print(find_max([6,2,1,5,0]))
#
#
#
# def count_even(list_):
#     counter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             counter +=1
#     return counter
# print(count_even([2,2,3,4,2,1,0]))
#
#
# def unique(list_):
#     new_list =[]
#     for i in list_:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
# print(unique([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]))

# Графический интерфейс

import tkinter as tk
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):#функция для повторений
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1+num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, command = add)
button_add.place(x =100, y =200) # ещё есть grid, pack
button_sub = tk.Button(window, text="-",width=2, height=2,command=sub)
button_sub.place(x =150, y =200)
button_mul = tk.Button(window, text="*",width=2, height=2,command=mul)
button_mul.place(x =200, y =200)
button_div = tk.Button(window, text="/",width=2, height=2, command=div)
button_div.place(x =250, y =200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100,y =75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100,y =150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100,y =300)
number1 = tk.Label(window, text ="Введите первое число:")
number1.place(x=120, y =50)
number2 = tk.Label(window, text ="Введите второе число:")
number2.place(x=120, y =125)
answer = tk.Label(window, text ="Введите ответ:")
answer.place(x=145, y =275)
window.mainloop()