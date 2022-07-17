# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.
# Пример:
# 100
# 10
# 200
# Вывод:
# 8

def is_number(value):  # Определяет является ли строка числом
    try:
        float(value)
        return True
    except:
        return False


def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input()
    while not is_number(result) or int(result) < 1:
        result = input('Неверный ввод! Введите число > 1: ')
    return float(result)


def year_period(contribution, percent, desired_amount):  # Основная функция для рассчета лет
    result = 0
    while contribution < desired_amount:
        contribution = contribution * (percent / 100) + contribution
        result += 1
    return result


print('Введите размер вклада в рублях: ')
contribution = correct_value()
print('Введите процент ежегодного увеличения: ')
percent = correct_value()
print('Введите желаемую сумму: ')
desired_amount = correct_value()
print(f'Колличество лет до получения желаемой суммы: '
      f'{year_period(contribution, percent, desired_amount)}')
