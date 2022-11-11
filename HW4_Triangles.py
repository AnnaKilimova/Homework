# 1 Вывести треугольник #1 с шириной N с помощью цикла while

n = int(input('Enter n: '))

k = n
i = 0

print('1)')

while i < k:
    print('*' * k)
    k -= 1

# 2 Вывести треугольник #2 с шириной N с помощью цикла while

k = n
i = 1

print('2)')

while i <= k:
    print('*' * i)
    i += 1

# 3 Вывести треугольник #3 с шириной N с помощью цикла while

k = n
i = 0
j = 0

print('3)')

while i < k:
    print(' ' * j + '*' * (k))
    k -= 1
    j += 1

# 4 Вывести треугольник #4 с шириной N с помощью цикла while

k = n
i = 0
j = 1

print('4)')

while i < k:
    print(' ' * (k-1) + '*' * j)
    k -= 1
    j += 1









