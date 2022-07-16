# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# 5! = 120

def is_number(value):  # Определяет является ли строка числом int
    try:
        int(value)
        return True
    except:
        return False


def correct_value():  # Позволяет ввести в строку только числовое значение int больше нуля
    result = input('Введите целое число > 0: ')
    while not is_number(result) or int(result) < 0:
        result = input('Неверный ввод! Введите целое число > 0: ')
    return int(result)


def factorial(number):
    if number == 1:
        return 1
    else:
        result = number * factorial(number - 1)
        return result


print(factorial(correct_value()))
