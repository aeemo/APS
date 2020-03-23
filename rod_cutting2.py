

N=int(input())
R=[0]*(N+1)
for i in range(2,N+1):
	for j in range(1,(i//2)+1):
		R[i]=max(R[i],j*(i-j),j*R[i-j])
print(R[N])