n=int(input());m=list(map(int,input().split()));dp=[0 for i in range(n)]
for i in range(n):
	for j in range(i):
		if m[i]>m[j]:dp[i]=max(dp[i],dp[j])
	dp[i]+=1
print(max(dp))