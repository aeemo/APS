#include<iostream>
#include <bits/stdc++.h> 

int main() {
    int t,n,m,i,k,P;
    int a;
    int j,count;
    int eo[2];
    
    
    scanf("%d",&t);
    
    for(k=0;k<t;k++)
    {
        eo[0]=0;
        eo[1]=0;
       scanf("%d%d",&n,&m);
       for (j=0;j<n;j++)
       {
           scanf("%d",&a);
           count= __builtin_popcount(a);
           
           if( count%2==0)
           eo[0]++;
           
       }
       eo[1]=n-eo[0];
    for(i=0;i<m;i++)
    {
        scanf("%d",&P);
        count= __builtin_popcount(P);
       if (count%2==0)
       {
       printf("%d",eo[0]);
       printf(" ");
       printf("%d\n",eo[1]);
       }
       else
       {
       printf("%d",eo[1]);
       printf(" ");
       printf("%d\n",eo[0]);
       }
       
       
    }
    }
    
    
	
	return 0;
}
