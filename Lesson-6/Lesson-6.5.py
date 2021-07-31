# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'Канцелярия'

    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def draw(self):
        print('Начинаем рисовать карандашом')

class Pen(Stationery):
    def draw(self):
        print('Начинаем рисовать ручкой')

class Handle(Stationery):
    def draw(self):
        print('Начинаем рисовать маркером')

pen_1 = Pen()
print(pen_1.title)
pen_1.draw()

pencil_1 = Pencil()
print(pencil_1.title)
pencil_1.draw()

handle_1 = Handle()
print(handle_1.title)
handle_1.draw()

paints_1 = Stationery()
print(paints_1.title)
paints_1.draw()