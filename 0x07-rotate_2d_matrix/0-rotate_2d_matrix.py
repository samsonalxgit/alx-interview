#!/usr/bin/python3

"""2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place."""
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return

    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

rotate_2d_matrix(matrix)
print(matrix)

