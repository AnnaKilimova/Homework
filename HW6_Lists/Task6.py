# Задание 6: Запросить у пользователя число N. Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
# Вывести эти числа.

N = int(input('Enter a number: '))
A = []

for _ in range(N):
   A.append(int(input('Enter a number: ')))

C_max = A[0]
C_min = A[0]

for i in range(len(A)):
   if C_min > A[i]:
      C_min = A[i]

   if C_max < A[i]:
      C_max = A[i]

print(C_min, C_max)
