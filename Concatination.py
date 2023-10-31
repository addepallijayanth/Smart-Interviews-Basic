# Read input
N = int(input())
A = list(map(int, input().split()))

# Duplicate the array
B = A + A

# Print the elements of the B array separated by space
print(*B)
