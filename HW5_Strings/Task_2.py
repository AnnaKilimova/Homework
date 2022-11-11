# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

a = str(input('Enter a text:'))

b = str(input('Enter a searchWord:'))

if a.find(b) != -1:
    print('YES')
else:
    print('NO')