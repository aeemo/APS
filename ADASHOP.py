t=int(input())
for _ in range(t):
    r,c=map(int,input().strip().split())
    a=[[2,2],[1,3],[3,1],[4,2],[5,1],[1,5],[2,6],[1,7],[7,1],[6,2],[7,3],[8,2],[2,8],[3,7],[4,8],[8,4],[7,5],[8,6],[6,8],[7,7],[8,8]]
    if r==1 and c==1:
            print(len(a))
            for i in range(len(a)):
                print(a[i][0],a[i][1])
    else:
            print(len(a)+2)
            q=(r+c)//2
            print(q,q)
            print(1,1)
            for i in range(len(a)):
                print(a[i][0],a[i][1])
            