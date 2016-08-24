#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
	int n;
	int cnt[26] = { 0 };
	cin >> n;
	vector<string> s(n);
	for (int i = 0; i < n; i++)
		cin >> s[i];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < s[i].size(); j++) {
			cnt[s[i][j] - 'A']++;
		}
	}
	vector<char> c;
	for (int i = 0; i < 26; i++) {
		if (cnt[i] > 0) {
			c.push_back((char)('A' + i));
		}
	}
	for (int i = 0; i < c.size(); i++)
		cout << c[i] << ' ';

	return 0;
}