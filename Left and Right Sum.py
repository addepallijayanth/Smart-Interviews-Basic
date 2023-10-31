# Function to calculate the prefix sum of an array
def calculate_prefix_sum(arr, n):
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    return prefix_sum

# Function to calculate the suffix sum of an array
def calculate_suffix_sum(arr, n):
    suffix_sum = [0] * n
    suffix_sum[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]
    return suffix_sum

# Input
n = int(input())
arr = list(map(int, input().split()))

# Calculate prefix sum and suffix sum arrays
prefix_sum = calculate_prefix_sum(arr, n)
suffix_sum = calculate_suffix_sum(arr, n)

# Calculate B array
b_arr = []
for i in range(n):
    left_sum = prefix_sum[i - 1] if i > 0 else 0
    right_sum = suffix_sum[i + 1] if i < n - 1 else 0
    b_i = abs(left_sum - right_sum)
    b_arr.append(b_i)

# Output the B array
print(*b_arr)
