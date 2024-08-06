numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # от двух - потому что простое число должно делиться на 1
        if n % i == 0:
            return False
    return True


primes = []
not_primes = []

for i in numbers:
    if is_prime(i):
        primes.append(i)
    else:
        not_primes.append(i)

print(primes, ' Простые числа')
print(not_primes, ' Числа, не относящиеся к простым')
