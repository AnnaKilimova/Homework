# Задание 2. Запросить у пользователя текст и записать его в файл data.txt

with open('data.txt', 'w') as f:
    f.write(input('Enter a text:'))
