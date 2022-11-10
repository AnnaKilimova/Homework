# Задание 1: Запросить у пользователя 5 чисел и записать их в список

list = []

for _ in range(5):
    list.append(int(input('Enter a number: ')))

print(list)