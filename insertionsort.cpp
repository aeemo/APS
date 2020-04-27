#include<iostream>

void insertionsort(int a[], int n)  
{  
    int i, key, j;  
    for (i = 1; i < n; i++) 
    {  
        key = a[i];  
        j = i - 1;  
  
        while (j >= 0 && a[j] > key) 
        {  
            a[j + 1] = a[j];  
            j = j - 1;  
        }  
        a[j + 1] = key;  
    }  
} 

int main(int argc, char *argv[]) {
	int i;
 int a[]={1,7,3,96,0,34,67,32,24,9};
 insertionsort(a,10);
 
	 for(i=0;i<10;i++)
	 {
 	printf("%d\t",a[i]);
	 }	
	
}
