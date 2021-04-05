import numpy as np

def rel_alt(input_matrix):
    row, col = input_matrix.shape
    if row<100 and col<100:
        print(input_matrix)
        temp_matrix=input_matrix.flatten()
        maximum1 = max(temp_matrix)
        maximum2 = max(temp_matrix, key=lambda x: min(temp_matrix) - 1 if (x == maximum1) else x)
        minimum1 = min(temp_matrix)
        minimum2 = min(temp_matrix, key=lambda x: 1-min(temp_matrix) if (x == minimum1) else x)

        for i in range(len(temp_matrix)):
            if temp_matrix[i]==maximum1:
                temp_matrix[i]=2
            elif temp_matrix[i]==maximum2:
                temp_matrix[i]=1
            elif temp_matrix[i]==minimum1:
                temp_matrix[i] =-2
            elif temp_matrix[i]==minimum2:
                temp_matrix[i] =-1
            else:
                temp_matrix[i] =0
        output_matrix=np.array(temp_matrix)
        output_matrix = output_matrix.reshape(row, col)

    return output_matrix

matrix= np.array([[ 3, 1, 4, 3],[0, 2, 4, 1],[1, 2, 1, 4],[4, 1, 4, 0]])
rel_alt(matrix)