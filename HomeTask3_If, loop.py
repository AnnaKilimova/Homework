#Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и
# первые два числа делятся на 3, то вывести yes, иначе no

a = int(input('Enter a number a:'))
b = int(input('Enter a number b:'))
c = int(input('Enter a number c:'))

if a > 10 and a % 3 == 0 and b > 10 and b % 3 == 0 and c > 10:
    print('yes')
else:
    print('no')

#Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.

a = int(input('Enter a number a:'))
b = int(input('Enter a number b:'))
c = int(input('Enter a number c:'))
max = 0

if max < a and a > b and a > c:
    max = a
    print('a = ', a, 'b = ', b, 'c = ', c, 'max = ', max)
elif b > c:
    max = b
    print('a = ', a, 'b = ', b, 'c = ', c, 'max = ', max)
elif b < c:
    max = c
    print('a = ', a, 'b = ', b, 'c = ', c, 'max = ', max)
else:
    print('a = ', a, 'b = ', b, 'c = ', c, 'max = ', max)

# Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

a = int(input('Enter a number a:'))
b = int(input('Enter a number b:'))
sum = 0

while a <= b:
    sum += a
    if a % 2 != 0:
        a += 1
        continue
    else:
        a += 1

print(sum)