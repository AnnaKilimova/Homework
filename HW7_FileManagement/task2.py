# Задание 2. Запросить у пользователя текст и записать его в файл data_text.txt

with open('data_text.txt', 'w') as f:
    f.write(input('Enter a text:'))
