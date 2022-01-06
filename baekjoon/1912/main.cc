// Copyright 2018 Inhyeok Bang
// Baekjoon no. 1912 (https://www.acmicpc.net/problem/1912)

#include <algorithm>
#include <cstdio>
#include <vector>

using std::vector;

vector<int> dp;

int main() {
  int n, result;

  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    int a;
    scanf("%d", &a);
    dp.push_back(a);

    if (i == 0)
      continue;
    else if (dp[i - 1] > 0)
      dp[i] = dp[i - 1] + dp[i];
  }

  printf("%d\n", *max_element(dp.begin(), dp.end()));
}
