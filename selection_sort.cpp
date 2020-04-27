#include<iostream>


void selectionsort(int a[], int n)  
{  
    int i, j, min,t;    
    for (i = 0; i < n-1; i++)  
    {   
        min = i;  
        for (j = i+1; j < n; j++)  
        if (a[j] < a[min])  
            min = j;  
        t=a[min];
        a[min]=a[i];
        a[i]=t;	        
    }  
}  

int main(int argc, char *argv[]) {
	int i;
 int a[]={1,7,3,96,0,34,67,32,24,9};
 selectionsort(a,10);
 
	 for(i=0;i<10;i++)
	 {
 	printf("%d\t",a[i]);
	 }	
	
}
 
