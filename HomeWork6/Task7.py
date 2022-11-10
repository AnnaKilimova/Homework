# Задание 7: Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример: > 'Lorem 222 ipsum, 1234 dolor 1 sit amet Количество чисел: 3

N = input('Enter a text: ')
quantity = 0

print(N.split())

for i in range(len(N.split())):
    if N.split()[i].isdigit() == True:
        quantity += 1

print(quantity)




     # print(N.split()[i].isdigit())


