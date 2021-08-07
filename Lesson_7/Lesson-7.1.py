class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return f'{self.matrix_list}'


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix1)