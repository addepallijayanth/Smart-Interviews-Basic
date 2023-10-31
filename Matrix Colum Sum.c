#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

   int n,m,i,j;
    long long a[100][100];
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
    {
        scanf("%lld",&a[i][j]);
    }
    }
    
  for(j=0;j<m;j++)
{int sum=0;
    for(i=0;i<n;i++)
    {
        sum=sum+a[i][j];
    }
    printf("%d\n",sum);
}
}
