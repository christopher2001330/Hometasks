import random
print("Добро пожаловать к аборигенам!")
print("-----------------------------")


def find_pairs(mine):
    pairs = []
    for n in range(1, mine):  # Перебор всех возможных значений n
        for m in range(n+1, mine):  # Перебор всех возможных значений m
            if mine%(n + m) == 0:
                pairs.append(f"{n}+{m}")  # Добавляем пару в список, если условие выполнено
    return pairs


def main():
    mine = random.randint(3, 20)  # Случайное число от 3 до 20
    print(f"Число в первой вставке: {mine}")

    pairs = find_pairs(mine)

    if pairs:
        print(f"Пары чисел, для которых {mine} кратно их сумме:")
        for pair in pairs:
            print(pair)
    else:
        print(f"Для числа {mine} нет подходящих пар.")

#It was really hard for me
main()


