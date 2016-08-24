t = int(input())
for i in range(t):
	a = sorted(list(map(int, input().split())))
	if abs(a[1] - a[3]) >= 4: print('KIN')
	else: print(sum(a[1:4]))