# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано
# положительное целое число).

def read_last(lines, file):

    sum = 0

    with open(file) as f:
        for line in iter(f.readline, ''):
            sum += 1
    print(f'всего строк: {sum}')

    with open(file) as f:
        data = f.readlines()
    data = ''.join(data[(sum - lines):])
    return data

print(read_last(int(input('Enter lines:')), "file.txt"))













# def change(lst):
#     n = 0
#     lst[-1], lst[n] = lst[n], lst[-1]
#     return lst
#
# print(change([1, 2, 3, 4, 5]))