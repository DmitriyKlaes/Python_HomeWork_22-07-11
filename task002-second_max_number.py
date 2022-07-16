# Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.
# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7

def second_max_number(list):
    max, second_max = list[0], list[1]
    if max < second_max:
        max, second_max = second_max, max
    for i in list[2:]:
        if max < i:
            second_max = max
            max = i
        elif second_max < i:
            second_max = i
    return second_max


list_1 = [1, 7, 9, 0]
print(second_max_number(list_1))
