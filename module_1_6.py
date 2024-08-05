# элементы хранялтся пармами - словарь
phone_book = {'Denis': 88005553535, 'Max':88005553534} #[1,2,3,4]
print(phone_book) #Ключ + значение, ключ не может быть изменяемым
print (phone_book['Denis'])
phone_book['Denis'] = 1513489346
print(phone_book) #Значение можно менять
phone_book['Anton'] = 85993473472
print(phone_book) # если элемент не существует, то добавляется
del phone_book ['Anton']
print(phone_book)
phone_book.update({'Sasha': 15889237549,
                   'Alex' : 12490842029})
print(phone_book)
print(phone_book.get('Denis'))
print(phone_book.get('Kamila'))
phone_book.pop('Alex')
print(phone_book)
list_ = [1,2,3]
list_.pop(0)
print(list_)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())


#МНОЖЕСТВА
set_ ={1,2,3,4,5,1,2,3,4, 'String', True, (1,2,3)}
list_ = [1,1,1,1,2,3,2,2]
list_ = set(list_)
print(list_)
print(list_.discard(1)) #можно использовать remove, pop
print(list_)
print(list_.add(5))
print(list_)