def final(a): 
          
    i=0

    neo=[]
    
    while(i<n-1):
        neo.append(a[i])
        if a[i]=='R' or a[i]=='L':
            for j in range(i+1,n):
                if a[j]=='L' or a[j]=='R':
                    j+=1
                else:
                    break
        if a[i]=='D' or a[i]=='U':
            for j in range(i+1,n):
                if a[j]=='D' or a[j]=='U':
                    j+=1
                else:
                    break
        i=j
    
    h=len(a)
    if a[h-2]=='R' or a[h-2]=='L':
        if a[h-1]=='D' or a[h-1]=='U':
            neo.append(a[h-1])
    if a[h-2]=='D' or a[h-2]=='U':
        if a[h-1]=='R' or a[h-1]=='L':
            neo.append(a[h-1])
    return neo

t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    
    gif=[0,0]
    
    st=final(list(s.rstrip()))
    
    for i in range(len(st)):
        if st[i]=='L':
            gif[0]-=1
        if st[i]=='R':
            gif[0]+=1
        if st[i]=='U':
            gif[1]+=1
        if st[i]=='D':
            gif[1]-=1
    print(gif[0],gif[1])    
        
        