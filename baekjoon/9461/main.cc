// Copyright 2018 Inhyeok Bang
// Baekjoon no. 9461 (https://www.acmicpc.net/problem/9461)

#include <cstdio>
#include <vector>

using std::vector;

vector<__int64_t> dp(5);

int main() {
  int t;
  unsigned int n;

  scanf("%d", &t);

  for (int i = 0; i < t; ++i) {
    dp[0] = dp[1] = dp[2] = 1;
    dp[3] = dp[4] = 2;
    scanf("%d", &n);

    if (n <= dp.size()) {
      printf("%ld\n", dp[n - 1]);
    } else {
      for (int j = dp.size(); j < n; ++j) {
        dp.push_back(dp[j - 1] + dp[j - 5]);
      }
      printf("%ld\n", dp[n - 1]);
    }
  }
}
