# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

# Два варианта решения.

def my_func(num1, num2, num3):
    """
    Функция вычисляет сумму наибольших двух чисел из принятых в качестве аргумента путем сортировки списка по возрастанию
    и сложения двух числе, стоящших на позициях 0 и 1.
    :param num1: float, любое число
    :param num2: float, любое число
    :param num3: float, любое число
    :return: float, сумма двух наибольших аргументов
    """
    my_list = [num1, num2, num3]
    my_sort = sorted(my_list, reverse=True)
    my_sum = my_sort[0] + my_sort[1]
    return my_sum

a = my_func(1.5, 15, -48)
print(a)

# Решение через if-else:
def my_func_new(num1, num2, num3):
    """
    Функция выбирает два наибольших числа из трех путем их сравнения друг с другом и вычисляет сумму.
    :param num1: float, любое число
    :param num2: float, любое число
    :param num3: float, любое число
    :return: float, сумма двух наибольших чисел
    """
    my_list = []
    my_sum = None
    if num1 > num3 and num2 > num3:
        my_list = [num1, num2]
    elif num1 > num2 and num3 > num2:
        my_list = [num1, num3]
    else:
        my_list = [num2, num3]
    my_sum = sum(my_list)
    return my_sum

b = my_func_new(1.3, 0.2, -3)
print(b)

