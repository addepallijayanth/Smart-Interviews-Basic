# Function to print the matrix elements in zig-zag order
def print_zigzag_matrix(matrix, n, m):
    for i in range(n):
        if i % 2 == 0:  # Even rows (left to right)
            for j in range(m):
                print(matrix[i][j], end=" ")
        else:  # Odd rows (right to left)
            for j in range(m - 1, -1, -1):
                print(matrix[i][j], end=" ")

# Input
n, m = map(int, input().split())
matrix = []

# Read the matrix elements
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the function to print the matrix in zig-zag order
print_zigzag_matrix(matrix, n, m)
