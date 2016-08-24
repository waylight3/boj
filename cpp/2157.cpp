#include <cstdio>
#include <vector>
using namespace std;

int dp[100010];
vector<pair<int, int>> cost[100010]; // cost[i] = (a, b) : from a to i, cost is b
int n, m, k;

int solve(int x) {

}

int main() {
	int a, b, c;

	memset(dp, -1, sizeof(dp));
	scanf("%d %d %d", &n, &m, &k);

	for (int i = 0; i < k; i++) {
		scanf("%d %d %d", &a, &b, &c);
		if (a > b) cost[b].push_back(make_pair(a, c));
	}

	return 0;
}