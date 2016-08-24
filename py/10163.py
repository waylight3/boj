m=[[0 for i in range(101)] for j in range(101)]
n=int(input())
for i in range(n):
	a,b,c,d=map(int,input().split())
	for y in range(b,b+d):
		for x in range(a,a+c):
			m[y][x]=i+1
for i in range(n):
	print(sum([row.count(i+1) for row in m]))