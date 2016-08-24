n=int(input())
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()))
for i in range(1,n):
	if a[i]-b[i]!=a[0]-b[0]:print('impossible');exit()
print('possible')