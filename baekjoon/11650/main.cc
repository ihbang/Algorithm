// Copyright 2018 Inhyeok Bang
// Baekjoon no. 11650 (https://www.acmicpc.net/problem/11650)

#include <algorithm>
#include <cstdio>
#include <tuple>
#include <vector>

using std::tuple;
using std::vector;

int main() {
  int n;
  vector<tuple<int, int> > v;

  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    int a, b;
    tuple<int, int> t;

    scanf("%d %d", &a, &b);
    t = std::make_tuple(a, b);
    v.push_back(t);
  }

  sort(v.begin(), v.end());

  for (auto k : v) {
    printf("%d %d\n", std::get<0>(k), std::get<1>(k));
  }
}
