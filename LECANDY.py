T=int(input())
for i in range(T):
    n,c=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    if sum(a)<=c:
        print('Yes')
    else:
        print('No')
