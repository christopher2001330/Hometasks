my_dict = {'Отлично':85, 'Хорошо': 70, 'Удовлетворительно': 60}
print(my_dict)
print(my_dict['Отлично'])
my_dict['Неудовлетворительно'] = 59
print(my_dict)
my_dict.update({'Ужасно':45,
            'Кошмарно':30})
print(my_dict)
print(my_dict['Кошмарно'])
del my_dict['Кошмарно']
print(my_dict)

#Множества
my_set = {1,2,2,3,3,4,5,5,5, "Turn on", False}
print(my_set)
print(my_set.add(6))
print(my_set.add(7))
print(my_set)
print(my_set.discard(5))
print(my_set)
