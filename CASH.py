# cook your dish here

t=int(input())

for _ in range(t):
    N,K=map(int, input().strip().split())
    A=list(map(int, input().strip().split()))
    C=sum(A)%K
    print(C)