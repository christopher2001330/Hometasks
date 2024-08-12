# def print_params(*params): # *args, **kwards
#     print(*params) #* звездочка - если не уверен сколько будет параметров, часто больше семи параметров
#
# print_params(1,2,3,4,5,6,7)

# def print_params(a,b,c):
#     print(a,b,c)
#
#
# list_ = [1,2,3]
# print_params(*list_)

# def print_params(**kwards):
#    for key, value in kwards.items():
#        print(key, value)
#
#
#
# dict_ = {'a': 1, 'b': 2, 'c' :3}
# print_params(**dict_)
def print_params(a,b,c):
    print(a,b,c)
list_ =[1,2]
dict_ ={'c':3}
print_params(*list_, **dict_)