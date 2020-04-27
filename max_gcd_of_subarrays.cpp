#include <bits/stdc++.h> 
using namespace std; 
  

int gcd(int a, int b) 
{ 
    if (b == 0) { 
        return a; 
    } 
    return gcd(b, a % b); 
} 
  
void findMaxGCD(int arr[], int n) 
{ 
    int maxGCD = 0; 
    for (int i = 0; i < n - 1; i++) { 
        int val = gcd(arr[i], arr[i + 1]);  
        if (val > maxGCD) { 
            maxGCD = val; 
        } 
    } 
    cout << maxGCD << endl; 
} 
  

int main() 
{ 
    int arr[] = { 2,5,7,9,4,14};  
    int n = sizeof(arr) / sizeof(arr[0]); 
    findMaxGCD(arr, n); 
    return 0; 
}
