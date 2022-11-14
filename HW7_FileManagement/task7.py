import re
import string

frequency = {}
document_text = open('data.txt', 'r')
text_string = document_text.read().lower()

print(text_string.split(sep=' '))

b = text_string.split(sep=' ')

c = []

for i in range(len(b)):
    if not b[i] in c:
        c.append(b[i])
    else: continue
print(c)

for j in range(len(c)):
    match_pattern = re.findall(c[j], text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    # for words in frequency_list:
    #     print(words, frequency[words])

for key, value in frequency.items():
    print(key, "=", value)

# print(frequency_list)
