#ДЗ 12. Реализация функции map

def custom_map(a, b):

    c = len(a) if len(a) < len(b) else len(b)

    d = []

    for i in range(c):
        d.append((a[i] + b[i]))

    return d

print(custom_map([1, 2, 3, 4, 5], [5, 4, 3]))








