# Read input number N
N = int(input())

# Function to reverse the number
def reverse_number(number):
    if number < 0:
        return int(str(number)[::-1][:-1]) * -1
    else:
        return int(str(number)[::-1])

# Call the function and print the reversed number
print(reverse_number(N))
