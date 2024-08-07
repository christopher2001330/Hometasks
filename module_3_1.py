a = 5
b = 10


def printer():
    global a, b
    a = 'Str'
    b = 'Str 2'
    c = 15
    d = 20
    print(c, d, 'Local')
    print(a, b, 'global')

print(a, b)
printer()
print(a, b)