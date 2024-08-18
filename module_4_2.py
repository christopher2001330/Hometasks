def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # inner_function() # Выводит принт

inner_function() # Выводит ошибку
test_function()