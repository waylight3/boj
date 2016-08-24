dp={}
def solve(s):
	global dp
	if s in dp: return dp[s]
	if len(s) == 0: return 1
	if len(s) == 1: return 0
	p = 0
	for i in range(1,len(s)):
		if s[i] != s[p]:
			if i - p > 1:
				r = solve(s[:p]+s[i:])
				if r == 1: dp[s] = 1; return 1
			p = i
	if p == 0: dp[s] = 1; return 1
	dp[s] = 0;
	return 0
for i in range(int(input())): print(solve(input()))