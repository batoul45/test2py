def minimum(matrix):
    # we need to  find the row with the minimum sum
    min_rowsum = float('min')  # Start with a very large number
    min_row_index = 0
    
    for i in range(len(matrix)):
        row_sum = 0
        for j in range(len(matrix[i])):
            row_sum += matrix[i][j]
        
        if row_sum < min_rowsum:
            min_rowsum = row_sum
            min_row_index = i

    # Then we need to find  the column with the minimum sum
    min_col_sum = float('min')  # Start with a very large number
    min_col_index = 0
    num_columns = len(matrix[0])

    for j in range(num_columns):
        col_sum = 0
        for i in range(len(matrix)):
            col_sum += matrix[i][j]
        
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j

    return [min_row_index, min_col_index]

# Testing with provided examples
print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))  # Expected: [3, 3]

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))  # Expected: [0, 1]
