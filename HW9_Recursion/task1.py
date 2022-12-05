# Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes'
# если number является степенью двойки, иначе 'no'. Запрещено пользоваться функцией или
# оператором возведение в степень.
def is_power_of_two(n):
    if(n == 1):
        return 'yes'
    elif(n>1 and n<2):
        return 'no'
    else:
        return is_power_of_two(n / 2)

print(is_power_of_two(125))

