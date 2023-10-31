#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
    int n,ptr;
    long long factorial=1;
    scanf("%d",&n);
    for(ptr=1;ptr<=n;ptr++)
    {
        factorial*=ptr;
    }
    printf("%lld",factorial);
}
