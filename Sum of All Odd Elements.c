#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,i;
    long a[100],sum=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%ld",&a[i]);
    
    }
    for(i=0;i<n;i++)
    {
        if(a[i]%2!=0)
        {
            sum=sum+a[i];
        }
    }
    printf("%ld",sum);
}
