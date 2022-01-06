// Copyright 2018 Inhyeok Bang
// Baekjoon no. 2193 (https://www.acmicpc.net/problem/2193)

#include <cstdio>
#include <vector>

using std::vector;

vector<vector<__int64_t> > dp;

int main() {
  int n;

  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    vector<__int64_t> ele(2);
    dp.push_back(ele);
  }
  dp[0][0] = 0;
  dp[0][1] = 1;
  for (int i = 1; i < n; ++i) {
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1];
    dp[i][1] = dp[i - 1][0];
  }
  printf("%lld\n", dp[n - 1][0] + dp[n - 1][1]);
}
