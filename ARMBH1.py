# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().strip().split()))
    m=min(s)
    s=[i-m for i in s]
    print(sum(s))