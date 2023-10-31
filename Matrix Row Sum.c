#include<stdio.h>
int main()
{
    int n,m,i,j;
    long a[100][100];
    scanf("%d %d",&n,&m);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=m;j++)
        {
            scanf("%ld",&a[i][j]);
        }
    }
    for(i=1;i<=n;i++)
    {int sum=0;
        for(j=1;j<=m;j++)
        {
            sum=sum+a[i][j];
        }
        printf("%d\n",sum);
    }
}
