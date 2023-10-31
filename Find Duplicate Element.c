#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int i, j,n;
    long long a[300];
    scanf("%d", &n);
        for (i = 0; i < n; i++)
        scanf("%lld", &a[i]);
        for( i=0; i<n; i++)
        {
            for(j=i+1;j<n;j++)
            {
     if(a[i] == a[j])

     {printf("%lld",a[i]);
            break;}
        }
        }
}
