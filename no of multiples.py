def numberofmultiples(n):
    return n//3+n//5-n//15
n=int(input())
print(numberofmultiples(n))
