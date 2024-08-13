data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    total_sum = 0  # начальное значение

    if isinstance(structure, int): # учитываем числа
        return structure

    if isinstance(structure, str): # считаем длину строки
        return len(structure)


    if isinstance(structure, (list, tuple, set)):
        for item in structure:
            total_sum += calculate_structure_sum(item) # вытаскиваем значения, считаем их выше

    elif isinstance(structure, dict):
        for key, value in structure.items():
            total_sum += calculate_structure_sum(value) # вытаскиваем значения, считаем их выше
            total_sum += calculate_structure_sum(key) # вытаскиваем значения, считаем их выше

    
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)

# С первыми двумя if помог чат джипити. Я не понимаю как эти строчки считают значения, ведь там только return???