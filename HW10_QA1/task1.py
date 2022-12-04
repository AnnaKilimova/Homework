#ДЗ 11. Случайная строка

import random
import string

def get_random_string(s_r, length):
    return ''.join(random.choice(s_r) for _ in range(length))

string_random = string.ascii_uppercase + string.ascii_lowercase + string.digits

print(get_random_string(string_random, length = 7))
print(get_random_string(string_random, length = 10))
print(get_random_string(string_random, length = 12))

# Не понимаю (закомментила ниже) почему когда я прописываю параметры как *args, **kwargs функция не работает?

# def randStr(*args, **kwargs):
#     return ''.join(random.choice(args) for _ in range(kwargs))
#
# string_random = string.ascii_uppercase + string.ascii_lowercase + string.digits
#
# print(randStr(string_random, 7))