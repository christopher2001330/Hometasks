# for i in 1, 2, 3, 4:
#     print(i)# то же что в последовательности, i  это переборщик
# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in 'Hello':
# for i in list_:
# # print(i)
# if i == 'three':
#     list_.remove(i)
# for i in range(5):
#     print(i) # 0, 1, 2, 3, 4,
# for i in range(len(list_)):
#     list_[i] = ' :('
# for i in range(len(list_2)):
# sum_ += list_2[i]
# print()
for i in range(1, 11):  # start, stop, step i-1
    for j in range(1, 11):  # вложенные циклы j-1
        print(f'{i} x {j} ={i * j}')

dict_ = {'a' : 1, 'b' :2, 'c' :3}

for i, k in dict_.items():
    print(i, k)