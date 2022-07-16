# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def is_number(value):  # Определяет является ли строка числом
    try:
        float(value)
        return True
    except:
        return False


def correct_value():  # Позволяет ввести в строку только числовое значение с переводом в абсолют
    result = input('Введите вещественное число: ')
    while not is_number(result):
        result = input('Неверный ввод! Введите вещественное число: ')
    return abs(float(result))


def summ_numbers_in(number):  # Основной метод для поиска суммы цифр
    number = int(str(number).replace('.', ''))
    result = 0
    while number != 0:
        result = number % 10 + result
        number = number // 10
    return result


print(summ_numbers_in(correct_value()))
