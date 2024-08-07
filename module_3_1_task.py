
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    str_len = len(string)
    str_up = string.upper()
    str_down = string.lower()
    return str_len, str_up, str_down

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    return string_lower in list_to_search_lower

# Ввод строки
input_string = str(input("Введите строку: "))

# Вызов функции string_info и сохранение результата
result1 = string_info(input_string)
print(result1)

# Список строк, среди которых будем искать совпадение
# Передаем только строку из результата string_info, игнорируя длину строки
result2 = is_contains(input_string, [result1[1], result1[2]])
print(result2)

# Вывод количества вызовов
print(f'Функцию вызвали: {calls} раз')
