# Вариант 1 - рандомайзер

#import random
#my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#while 1 > 0:
   # number = random.choice(my_list)
    #if number >= 0:
       # print((number), "Число положительное")
    #else:
       # print((number), "Число отрицательное")
       # break
#print("Я за циклом")

#Варинат 2 - с индексом

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0

while index < len(my_list):
    number = my_list[index]
    if number < 0:
        break
    if number == 0:
        index += 1
        continue
    print(number)

    index += 1 #увеличение на 1
