// Copyright 2018 Inhyeok Bang
// Baekjoon no. 2751 (https://www.acmicpc.net/problem/2751)

#include <algorithm>
#include <cstdio>
#include <vector>

using std::vector;

int main() {
  int n;
  vector<int> v;

  scanf("%d", &n);
  v.resize(n);

  for (int i = 0; i < n; ++i) scanf("%d", &(v[i]));

  sort(v.begin(), v.end());

  for (auto k : v) {
    printf("%d\n", k);
  }
}
