# 1 Вывести треугольник #1 с шириной N с помощью цикла while

n = int(input('Enter n: '))

k = n
i = 0

print('1)')

while i < k:
    print('*' * k)
    k -= 1

print(n)
# 2 Вывести треугольник #2 с шириной N с помощью цикла while

k = n
i = 1

print('2)')

while i <= n:
    print('*' * i)
    i += 1