# cook your dish here
T=int(input())

for i in range(T):
    flag=0
    X,Y,K,N=map(int,input().strip().split())
    a=X-Y
    for j in range(N):
        pi,ci=map(int,input().strip().split())
        if a<=pi and K>=ci:
            flag=1
        
    if flag==0:
        print('UnluckyChef')
    else: print('LuckyChef')
   
        