# Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

a = str(input('Enter a word:'))

if a[::-1].lower() == a.lower():
    print('+')
else:
    print('-')