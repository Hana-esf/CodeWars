import numpy as np

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    else:
        det_result = 0
        temp_mat = np.delete(matrix, 0, axis=0)
        for i in range(len(matrix)):
            temp2_mat = np.delete(temp_mat, i, axis=1)
            det_result += (-1)**(i+2) * matrix[0][i] * determinant(temp2_mat)
    return det_result



#main
#geting the input 2D array
n = int(input('Enter the size of the matrix : '))
mat_row = []
matrix_input = [] 
for i in range(n):
    mat_row = [int(i) for i in input().split()]
    matrix_input.append(mat_row)

print('the result is : ',determinant(matrix_input))