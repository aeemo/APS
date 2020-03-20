#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
   long int n;
    int i;
    int * arr;
    scanf("%d",&n);      
    arr=(int*)malloc(n*sizeof(long int));
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
   
    int sum=0;
    
    for(i=0;i<n;i++)
    {
        while(arr[i]!=0)
        {
            arr[i]=arr[i]&(arr[i]-1);
            sum+=1;
        }
    }
    printf("%d",sum);
    
    return 0;
}