immutable_var = (1,2,3,"Hello world", False)
print(immutable_var)
# immutable_var[0]=50
# print(immutable_var) # вылезла ошибка так как кортедж - это неизменяемый массив
mutable_list = [1,2,3]
mutable_list[0] = 50
print(mutable_list) # тут все получилось, потому что список - изменяемый массив