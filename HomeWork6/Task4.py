# #Задание 4: Запросить у пользователя число N. Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

N = int(input('Enter N number: '))
A = []

for _ in range(N):
   A.append(int(input('Enter a number: ')))

print(A[::-1])
