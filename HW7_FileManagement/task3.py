# Задание 3. Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл
# numbers.txt через пробел

N = int(input('Enter a number: '))
n = " "

with open('numbers.txt', 'w') as f:
    for _ in range(N):
        f.write((input('Enter a number: ' '')) + ' ')
