#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

bool visited[1000010];

int main() {
	int f, s, g, u, d, now, cnt = 0;
	
	memset(visited, false, sizeof(visited));
	scanf("%d %d %d %d %d", &f, &s, &g, &u, &d);

	queue<int> q;
	q.push(s);

	while (!q.empty()) {
		for (int i = q.size(); i > 0; i--) {
			now = q.front(); q.pop();
			if (now == g) {
				printf("%d", cnt);
				return 0;
			}
			if (now + u <= f && !visited[now + u]) {
				visited[now + u] = true;
				q.push(now + u);
			}
			if (now - d > 0 && !visited[now - d]) {
				visited[now - d] = true;
				q.push(now - d);
			}
		}
		cnt++;
	}
	printf("use the stairs");

	return 0;
}