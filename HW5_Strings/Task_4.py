# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

a = input('Type text:')
b = ''

for i in range(0, len(a)):
    if a[i].isdigit():
        continue
    else:
        b += a[i]
print(b)