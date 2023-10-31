n=str(input())
l=len(n)
#print(l)
ans=0
for i in n:
    #print(i)
    ans+=int(i)**l
    #print(ans)
#print(ans)
if ans==int(n):
    print('Yes')
else:
    print('No')
