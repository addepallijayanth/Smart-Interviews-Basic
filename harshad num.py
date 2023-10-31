n=str(input())
addn=0
for i in n:
    addn+=int(i)
if int(n)%addn==0:
    print('Yes')
else:
    print('No')
