# name = input('Введите ваше имя: ')
# if name == 'Urban':
#     print ("Здрваствуйте, администратор")
# if name == 'Денис':
#     print ("Здравтсвуйте, преподователь")
# else:
#     print("Привет, ", name)
number = int(input("Введите число: ")) # Fizz, Buzz, FizzBuzz
if number % 3 == 0 and number % 5 == 0:
    print ('FizzBuzz')
elif number % 3 == 0:
    print ('Fizz')
elif number % 5 == 0:
    print ('Buzz') # or  не строгий and строгий
else:
    print("Число не подходит")




