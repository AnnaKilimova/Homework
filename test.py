# Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

a = int(input('Enter a number a:'))
b = int(input('Enter a number b:'))
sum = 0

while a <= b:
    if a % 2 != 0:
        a += 1
        continue
    else:
        sum += a
        a += 1
print(sum)

