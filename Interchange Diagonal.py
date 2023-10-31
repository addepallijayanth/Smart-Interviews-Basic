# Read input size of the matrix
n = int(input())

# Initialize an empty matrix
matrix = []

# Read the matrix elements
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Interchange diagonal elements
for i in range(n):
    # Swap elements on the diagonal (from top to bottom)
    matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]

# Print the resultant matrix
for row in matrix:
    print(" ".join(map(str, row)))
