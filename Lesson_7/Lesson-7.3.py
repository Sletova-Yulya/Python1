class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __str__(self):
        return f'Клетка с количеством ячеек {self.num_cells}'

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        if self.num_cells > other.num_cells:
            return Cell(self.num_cells - other.num_cells)
        else:
            return 'Невозможно произвести вычитание ячеек'

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        return Cell(round(self.num_cells / other.num_cells))

    def make_order(self, num_stars):
        if self.num_cells % num_stars == 0:
            return ('*' * num_stars + '\\n') * (self.num_cells // num_stars -1) + ('*' * num_stars)
        else:
            return (('*' * num_stars + '\\n') * (self.num_cells // num_stars) + ('*' * (self.num_cells % num_stars)))

cell1 = Cell(15)
cell2 = Cell(8)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell1 / cell2)
print(cell1 * cell2)
print(cell1.make_order(5))

