# Function to find the highest altitude the pilot can reach
def highest_altitude(N, arr):
    max_altitude = 0  # Initialize the maximum altitude to 0
    current_altitude = 0  # Initialize the current altitude to 0

    for i in range(N):
        current_altitude += arr[i]  # Update the current altitude

        # Update the maximum altitude if the current altitude is higher
        if current_altitude > max_altitude:
            max_altitude = current_altitude

    return max_altitude

# Input
N = int(input())
arr = list(map(int, input().split()))

# Find the highest altitude the pilot can reach
result = highest_altitude(N, arr)

# Output the result
print(result)
