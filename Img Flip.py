# Function to flip the image horizontally
def flip_horizontally(matrix):
    return [row[::-1] for row in matrix]

# Function to invert the image (0s to 1s, and 1s to 0s)
def invert_image(matrix):
    return [[1 - cell for cell in row] for row in matrix]

# Input
N, M = map(int, input().split())
image = []

# Read the matrix elements
for _ in range(N):
    row = list(map(int, input().split()))
    image.append(row)

# Perform the operations
image = flip_horizontally(image)
image = invert_image(image)

# Print the resultant matrix
for row in image:
    print(*row)
