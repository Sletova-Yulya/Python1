# 2. Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# 1 способ:
my_str = input('Введите любую последовательность элементов: ')
str_reversed = ''
symbols = list(my_str)
if len(my_str) % 2 == 0:
    for el in range(0, len(my_str), 2):
        symbols[el], symbols[el + 1] = symbols[el + 1], symbols[el]
else:
    for el in range(0, len(my_str) - 1, 2):
        symbols[el], symbols[el + 1] = symbols[el + 1], symbols[el]
str_reversed = ''.join(symbols)
print(str_reversed)

# 2 способ:
my_str = input('Введите любую последовательность элементов: ')
str_reversed = ''
symbols = list(my_str)
for el in range(len(my_str)):
    if (el % 2 == 0) and (el != len(my_str) - 1):
        symbols[el], symbols[el + 1] = symbols[el + 1], symbols[el]
str_reversed = ''.join(symbols)
print(str_reversed)