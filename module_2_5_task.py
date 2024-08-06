
def get_matrix(n=2, m=2, value=10):
    matrix = []
    for i in range(n):          # Цикл для строк
        row = []                # Создаем пустой список для строки
        for j in range(m):      # Цикл для столбцов
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)     # Добавляем строку в матрицу
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
