#include <iostream>


void bubblesort(int a[])
{
	int i,j,temp;
	for(i=0;i<10;i++)
	{
		for(j=i+1;j<10;j++)
		{
			if (a[j]<a[i])
			{
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
}

int main(int argc, char *argv[]) {
	int i;
 int a[]={1,7,3,96,0,34,67,32,24,9};
 bubblesort(a);
 
	 for(i=0;i<10;i++)
	 {
 	printf("%d\t",a[i]);
	 }	
	
}

