# Function to set rows and columns to zero in the new matrix
def set_zeros(matrix, n, m):
    # Initialize a new matrix with the same values as the input matrix
    new_matrix = [row[:] for row in matrix]

    # Determine which rows and columns need to be zeroed out
    rows_to_zero = set()
    columns_to_zero = set()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                columns_to_zero.add(j)

    # Set rows to zero in the new matrix
    for row_idx in rows_to_zero:
        new_matrix[row_idx] = [0] * m

    # Set columns to zero in the new matrix
    for col_idx in columns_to_zero:
        for i in range(n):
            new_matrix[i][col_idx] = 0

    return new_matrix

# Input
n, m = map(int, input().split())
matrix = []

# Read the matrix elements
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Call the function to set rows and columns to zero
result_matrix = set_zeros(matrix, n, m)

# Print the resultant matrix
for row in result_matrix:
    print(*row)
