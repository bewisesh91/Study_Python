def P3(matrix):
    for k in range(len(matrix)) :
        for i in range(len(matrix)-1) :
            for j in range(len(matrix[0])-1) :
                if matrix[i][j] > matrix[i+1][j+1] :
                    matrix[i][j], matrix[i+1][j+1] = matrix[i+1][j+1], matrix[i][j]
    return matrix
