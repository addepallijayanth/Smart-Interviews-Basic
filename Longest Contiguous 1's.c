# Function to find the length of the longest contiguous 1's
def longest_contiguous_ones(arr, n):
    max_length = 0  # Initialize the maximum length to 0
    current_length = 0  # Initialize the current length to 0

    for i in range(n):
        if arr[i] == 1:
            current_length += 1
        else:
            current_length = 0  # Reset the current length when a 0 is encountered

        # Update the maximum length if the current sequence is longer
        if current_length > max_length:
            max_length = current_length

    return max_length

# Input
n = int(input())
arr = list(map(int, input().split()))

# Find the length of the longest contiguous 1's
result = longest_contiguous_ones(arr, n)

# Output the result
print(result)
