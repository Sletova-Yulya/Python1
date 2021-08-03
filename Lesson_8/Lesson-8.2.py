# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))

try:
    if divider == 0:
        raise ZeroDivError("В качестве делителя введен ноль. Делить на ноль нельзя")
    quotient = dividend / divider
except ZeroDivError as zderr:
    print(zderr)
else:
    print(f'Результат деления: {quotient}')

