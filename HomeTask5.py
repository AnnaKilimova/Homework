# Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

a = str(input('Enter a word:'))

if a[::-1].lower() == a.lower():
    print('+')
else:
    print('-')

# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

a = str(input('Enter a text:'))

b = str(input('Enter a searchWord:'))

if a.find(b) != -1:
    print('YES')
else:
    print('NO')

# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

a = str(input('Enter a string:'))

if a.startswith('abc'):
    print(a.replace('abc', 'www'))
else:
    print(a + 'zzz')

# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

a = input('Type text:')
b = ''

for i in range(0, len(a)):
    if a[i].isdigit():
        continue
    else:
        b += a[i]
print(b)
