# Задание 3: Запросить у пользователя 10 чисел и записать их в список A. Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N

A = []
N = int(input('Enter N number: '))

for _ in range(10):
   A.append(int(input('Enter a number: ')))

print(A)

print(A.count(N))