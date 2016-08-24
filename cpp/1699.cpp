#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int dp[100000];

int solve(int n) {
	int& ret = dp[n];

	if (ret != 123456789) return ret;

	for (int i = 1; i * i <= n; i++) {
		ret = min(ret, solve(n - i * i)) + 1;
	}
	
	return ret;
}

int main() {
	int n;

	cin >> n;

	for (int i = 0; i <= n; i++) dp[i] = 123456789;
	for (int i = 1; i * i <= n; i++) dp[i * i] = 1;

	cout << solve(n);

	return 0;
}