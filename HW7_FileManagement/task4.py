# Задание 4. Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где
# одна строка = одно число

import random

f = open('random_numbers.txt', 'w')
f.write("\n".join(map(str, random.sample(range(1000), 100))))
f.close()





