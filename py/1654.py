k, n = map(int, input().split())
d=[]
for i in range(k):d.append(int(input()))
s=1;e=1000010
while s <= e:
	m = (s + e) // 2
	a = 0
	for c in d:a += c // m
	if a >= n:s = m + 1
	elif a < n:e = m - 1
print(m)