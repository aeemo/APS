t=int(input())


for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    a.sort()
    b.sort()
    s=0
    for i in range(n):
       s+=min(a[i],b[i]) 
       
    print(s)
