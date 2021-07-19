# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [el for el in range(100, 1001, 2)]

# 1. Вариант:
multiplic_func = reduce(lambda el, el1: el * el1, my_list)
print(multiplic_func)

# 2. Вариант:
def muliplication_num(prev_elem, elem):
    return prev_elem * elem

print(reduce(muliplication_num, my_list))