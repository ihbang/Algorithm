// Copyright 2018 Inhyeok Bang
// Baekjoon no. 11004 (https://www.acmicpc.net/problem/11004)

#include <algorithm>
#include <cstdio>
#include <vector>

int main() {
  int n, k;
  std::vector<int> v;

  scanf("%d %d", &n, &k);

  for (int i = 0; i < n; ++i) {
    int a;
    scanf("%d", &a);
    v.push_back(a);
  }
  std::nth_element(v.begin(), v.begin() + k - 1, v.end());
  printf("%d\n", v[k - 1]);
}
