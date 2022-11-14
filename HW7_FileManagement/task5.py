# Задание 5. Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

f = open('data_text.txt', 'r')

data = f.read().split()

print(data)

print(len(data))









