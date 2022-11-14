#Задание 6. Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

a = 0

f = open('data.txt', 'r')

data = list(map(int, f.read().split()))

for i in range(len(data)):
    a += data[i]

print(a)

