# Задание 1. Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

f = open('data.txt', 'r')

data = f.read().split()

numbers = []

for i in range(len(data)):
    if data[i].isdigit() == True:
        numbers.append(data[i])
    else:
        continue

print(numbers)