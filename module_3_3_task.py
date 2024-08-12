def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [55, 'Пример',True]
values_dict_partial = {'c': True}
values_list_2 = [54, 'Строка']

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


print_params(*values_list)
print_params(**values_dict_partial)


print_params(*values_list_2, 42)


