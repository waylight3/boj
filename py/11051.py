dp = [[0 for i in range(1010)] for j in range(1010)]

def comb(n, k):
	global dp
	if n == k or k == 0:
		return 1
	if dp[n][k] == 0:
		dp[n][k] = (comb(n - 1, k - 1) + comb(n - 1, k)) % 10007
	return dp[n][k]

n, k = map(int, input().split())
print(comb(n, k))