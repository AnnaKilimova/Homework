#Задание 6. Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

f = open('data_only_numbers.txt', 'r')

data = list(map(int, f.read().split()))

a = 0

for i in range(len(data)):
    a += data[i]

print(a)

