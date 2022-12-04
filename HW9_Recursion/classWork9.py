import time
from typing import List, Union, Optional

# def sum_all_sequences(number: Union[int, float]):
#     print(f'Number = {number}')
#     if number == 10:
#         return number
#     return sum_all_sequences(number + 1)
#
# print(sum_all_sequences(1))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(4))

# def fibonacci(n, numbers:Optional[List[int]] = None):
#     numbers.append(n)
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1, numbers) + fibonacci(n-2, numbers)
#
# lists = []
#
# print(fibonacci(4, lists))
# print(lists)

# def very_slow_function(max_number: int) -> int:
#     start = time.time()
#     result = 0
#     for i in range(max_number):
#         result += i
#     end = time.time()
#     print(f'max_number = {max_number} | time = {end - start}')
#     return result
#
# def get_run_time(func, *args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     print(f'func = {func} | time = {time.time() - start}')
#     return result
#
# print(get_run_time)
# get_run_time(very_slow_function, 10000000)
# print(very_slow_function(10000000))

#Декоратор
# def get_run_time(func):
#
#     def inner(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f'func = {func} | time = {time.time() - start}')
#         return result
#
#     return inner
#
# @get_run_time
# def function_to_be_used(name: str):
#     print('This is inside the function')
#     return f'Hello {name}'
#
# print(function_to_be_used('Petr'))

def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

# def say(name, surname):
#     print('hello', name, surname)
#
# say = table(header(say))
# say('Vasya', 'Ivanov')
# print(f'say = {say}')

#=

@header
@table
def say(name, surname):
    print('hello', name, surname)

say('Vasya', 'Ivanov')
print(f'say = {say}')

