# Задание 5: Запросить у пользователя 5 чисел и записать их в список A.
# Записать все числа из списка A которые больше 5 в список C

A = []
C = []

for i in range(5):
   A.append(int(input('Enter a number: ')))
   if A[i] > 5:
       C.append(int(A[i]))

print(A)
print(C)