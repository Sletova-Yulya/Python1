# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# Реализованы два варианта: с try-except и без него.

# Без обработки исключений:
def division_func():
    """
    Функция осуществляет деление целых чисел. Реализована проверка деления на ноль.
    :param numb_1: int Делимое
    :param numb_2: int Делитель
    :return: int. Частное от деления двух чисел.
    """
    numb_1 = int(input("Введите делимое: "))
    numb_2 = int(input("Введите делитель: "))
    if numb_2 == 0:
        print("Введено недопустимое значение для делителя")
        return
    else:
        quotient = numb_1 / numb_2
    return quotient

a = division_func()
print(a)

# С обработкой исключений конструкцией try - except, а так же возможность деления дробей:
def division_func_new():
    """
    Функция осуществляет деление целых чисел и дробей. Реализована обработка исключений: ZeroDivisionError и ValueError.
    :param numb_1: float, Делимое
    :param numb_2: float, Делитель
    :return: float, Частное от деления двух чисел.
    """
    try:
        numb_1 = float(input("Введите делимое: "))
        numb_2 = float(input("Введите делитель: "))
        quotient = numb_1 / numb_2
    except ZeroDivisionError:
        print("Введено неверное значение для делителя")
        return
    except ValueError:
        print("Вы ввели не число!")
        return
    return quotient

a = division_func_new()
print(a)