# Function to print the transpose of a matrix
def print_transpose_matrix(matrix, n, m):
    # Initialize a new matrix for the transpose
    transpose_matrix = [[0 for _ in range(n)] for _ in range(m)]

    # Compute the transpose
    for i in range(n):
        for j in range(m):
            transpose_matrix[j][i] = matrix[i][j]

    # Print the transpose matrix
    for i in range(m):
        for j in range(n):
            print(transpose_matrix[i][j], end=" ")
        print()

# Input
n, m = map(int, input().split())
matrix = []

# Read the matrix elements
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the function to print the transpose of the matrix
print_transpose_matrix(matrix, n, m)
