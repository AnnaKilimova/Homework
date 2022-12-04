# def sum_int(a = 4):
#     a += 1
#     print(a)
#
# sum_int(1)
# sum_int()
# sum_int()
# sum_int()

#Wrong
# def list_sum(numbers=[]):
#     numbers.append(1)
#     print(sum(numbers))
#
# list_sum([1, 2, 3]) #7
# list_sum() #1
# list_sum() #2
# list_sum() #3
# list_sum() #4

#Correct
# def list_sum(numbers=None):
#     if numbers is None:
#         numbers = []
#     numbers.append(1)
#     print(sum(numbers))
#
# list_sum([1, 2, 3]) #7
# list_sum() #1
# list_sum() #1
# list_sum() #1
# list_sum() #1

# def default_args_v2(*args, **kwargs):
#     print(args, kwargs)
#
# default_args_v2(1, 2, 3, 4, 5, 6, 7, 8, k=2, a=3)

#Чтобы изменить значение глобальной переменной:

x = 15

def local_view():
    global x

    x = 30
    print(f'local_view x = {x}')

print(f'1) global x = {x}')
local_view()
print(f'2) global x = {x}')

#nonlocal

# def local_view():
#     x = 10
#
#     print(f'local_view x = {x}')
#
#     def nonlocal_view():
#         nonlocal x #если не прописать последний x будет 10
#         x = 5
#         print(f'nonlocal_view x = {x}')
#
#     nonlocal_view()
#     print(f'x = {x}')
#
# local_view()
#
# def annotations(a: int, b: int = 10) -> int:
#     print(f'A = {a} Type = {type(a)} | B = {b} Type = {type(b)}')
#
#     return  a * b
# test = annotations('hello world', 2)
# c  = 4.5
# print(isinstance(c, str))
# print(isinstance(c, (float, int)))
# print(test, type(test))

# def foo(x: any):
#     return  x + 1
#
# numbers = [1, 2, 3, 4, -10]
#
# new_numbers = list(map(foo, numbers))
# print(new_numbers)

# foo = lambda a, b: a + b
#
# print(foo(5, 2))


# numbers = [1, 2, 3, 4, -10]
#
# new_numbers = list(map(lambda x: x + 1, numbers))
# print(new_numbers)


