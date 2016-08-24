#include <cstdio>
#include <cmath>

int main() {
	int n, c = 0;
	scanf("%d", &n);
	while (n > 0) {
		n -= (int)(sqrt(8 * n + 1) - 1) / 2;
		c++;
	}
	printf("%d", c);

	return 0;
}