# cook your dish here
T=int(input())


for i in range(T):
    sal=0
    X,N=map(int,input().strip().split())
    for  j in range(X,N,X):
        sal+=j
    print(sal)    