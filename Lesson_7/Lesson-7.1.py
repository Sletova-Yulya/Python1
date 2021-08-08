class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        string = ''
        for elem in self.matrix_list:
            string += f'{elem} \n'
        return string

    def __add__(self, other):
        result = []
        numbers = []
        if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
            for i in range(len(self.matrix_list)):
                for j in range(len(self.matrix_list[0])):
                    sum = other.matrix_list[i][j] + self.matrix_list[i][j]
                    numbers.append(sum)
                    if len(numbers) == len(self.matrix_list[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            return 'Матрицы невозможно сложить'


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix1)
print(matrix1 + matrix2)