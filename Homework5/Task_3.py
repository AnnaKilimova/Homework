# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

a = str(input('Enter a string:'))

if a.startswith('abc'):
    print(a.replace('abc', 'www'))
else:
    print(a + 'zzz')