# tuple_ = 1, 2, 3, 4, True, "String"
# list_ = [1, 2, 3, True, "String"]
# print (tuple) #Круглые скобки - неизменяемый список (кортедж)
# print(tuple_.__sizeof__())
# print(list_.__sizeof__())
tuple_ = ([1,2],0) +(1,2)
print(tuple_)
tuple_[0][0] =2
print(tuple_)
tuple_ = (1,2)*3
print(tuple_)