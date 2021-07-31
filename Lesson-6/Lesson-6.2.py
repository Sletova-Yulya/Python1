# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calc(self, depth, mass):
        '''
        Рассчитывает массу асфальта, необходимую для покрытия дороги с указанными параметрами
        :param depth: глубина в метрах
        :param mass: масса на 1 квадратный метр в тоннах
        :return: искомая масса асфальта
        '''
        total_mass = self._lenght * self._width * depth * mass
        return total_mass

road_1 = Road(3, 5)
print(road_1.mass_calc(0.2, 0.5))

road_2 = Road(10, 500)
print(road_2.mass_calc(0.05, 0.2))