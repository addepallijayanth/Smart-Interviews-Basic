# Input
N, i = map(int, input().split())

# Check if the ith bit is set
if (N & (1 << i)) != 0:
    print("true")
else:
    print("false")
