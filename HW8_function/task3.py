#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end»
# включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end):

    if start > end:
        sum = start
        start = end
        end = sum

    print(f'start = {start}, b = {end}')

    sum = 0

    for start in range(end+1):
        sum += start
    return sum

print(sum_range(int(input('Enter start number:')), int(input('Enter end number:'))))


