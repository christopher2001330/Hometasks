from .module1 import hello # . текущий каталог, : каталог выше
def good_word(name):
    hello(name)
    print("Ты лучший", name)

if __name__ == '__main__':
    good_word("Урбан")