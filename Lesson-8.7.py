# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real_part, imagine_part):
        self.real_part = real_part
        self.imagine_part = imagine_part
        self.comp_num = complex(real_part, imagine_part)

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imagine_part + other.imagine_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imagine_part * other.imagine_part,
                             self.real_part * other.imagine_part + other.real_part * self.imagine_part)

    def __str__(self):
        return f'{self.comp_num}'

comp_num1 = ComplexNumber(5, 6)
comp_num2 = ComplexNumber(10, 15)
print(comp_num1 + comp_num2)
print(comp_num1 * comp_num2)