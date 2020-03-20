#include <stdio.h>
int max(int a,int b,int c)
{
    if (a>b && a>c)
    return a;
    else if(b>a && b>c)
    return b;
    else if(c>a && c>b)
    return c;
    
}

void rod_cutting(int n)
{
    int i,j;
    int result[n];
    result[n]={0};
    for(i=2;i<=n;i++)
    {
        for(j=1;j<=n/2;j++)
        {
            result[i]=maxi(result[i],(i-j)*j,result[i-j]*j);
        }
    }
    printf(result[n]);
    
}
int main() {
    int n;
    scanf("%d",&n);
    rod_cutting(n)
	//code
	return 0;
}

