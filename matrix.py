class Matrix:
    def __init__(self, matrix, val=0):
        if isinstance(matrix, tuple):
            self._private_member = [
                [val for x in range(matrix[1])] for y in range(matrix[0])]
        else:
            self._private_member = matrix

    def __add__(self, matrix):
        #sprawdzenie wymiarow
        row_1 = len(self._private_member)
        col_1 = len(self._private_member[0])
        row_2 = len(matrix)
        col_2 = len(matrix[0])
        temp_matrix =[[0 for x in range(col_1)] for y in range(row_1)]
        if row_1 == row_2 and col_1 == col_2:
            for i in range(0, row_1):
                for j in range(0, col_1):
                    temp_matrix[i][j] = self._private_member[i][j] + matrix[i][j]
            return Matrix(temp_matrix)
        else:
            return None
        

    def __mul__(self, matrix):
        #sprawdzenie wymiarow
        row_1 = len(self._private_member)
        col_1 = len(self._private_member[0])
        row_2 = len(matrix)
        col_2 = len(matrix[0])
        temp_matrix =[[0 for x in range(row_1)] for y in range(row_1)]
        if col_1 == row_2:
            for i in range(0, row_1):
                for j in range(0, col_2):
                    for k in range(0, col_1):
                        temp_matrix[i][j] += self._private_member[i][k] * matrix[k][j]
            return Matrix(temp_matrix)
        else:
            return None

    def __str__(self):
        for i in range(len(self._private_member)):
            print(self._private_member[i])

    def __getitem__(self):
        return self._private_member

def transpose(matrix):
    new_cols = len(matrix)
    new_rows = len(matrix[0])
    temp_matrix = [[ 0 for j in range(new_cols)] for i in range(new_rows)]
    for i in range(new_cols):
        for j in range(new_rows):
            temp_matrix[j][i] = matrix[i][j]
    ret_matrix = Matrix(temp_matrix)
    return ret_matrix


matrix1 = [[1, 0, 2], [-1, 3, 1]]

print('Transpozycja macierzy 1:')
matrix1_transposed = transpose(matrix1)
matrix1_transposed.__str__()

print('\nSumowanie matrix1 z matrix2:')
matrix2 = Matrix((2,3), 1)
add_res_matrix = matrix2.__add__(matrix1)
add_res_matrix.__str__()

print('\nMnozenie matrix1 z [[3,1],[2,1],[1,0]]:')
matrix3 = [[3,1],[2,1],[1,0]]
matrix1_2 = Matrix([[1, 0, 2], [-1, 3, 1]])
mul_res_matrix = matrix1_2.__mul__(matrix3)
mul_res_matrix.__str__()

