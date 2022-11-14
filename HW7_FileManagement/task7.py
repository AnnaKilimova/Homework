# Задание 7. Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз 'привет' - 10 раз 'как' - 9 раз 'у' - 7 'world' - 4

import re
import string

f = {}
document_text = open('data_text.txt', 'r')
text_string = document_text.read().lower()
text_string_list = text_string.split(sep=' ')

print('text_string_list = ', text_string_list)

search_word = []

for i in range(len(text_string_list)):
    if not text_string_list[i] in search_word:
        search_word.append(text_string_list[i])
    else:
        continue
print('search_word = ', search_word)

for j in range(len(search_word)):
    match_pattern = re.findall(search_word[j], text_string)

    for word in match_pattern:
        count = f.get(word, 0)
        # print('count = ', count, 'word = ', word)
        f[word] = count + 1

for key, value in f.items():
    print(key, "=", value)


