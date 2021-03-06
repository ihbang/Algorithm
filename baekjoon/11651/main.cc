// Copyright 2018 Inhyeok Bang
// Baekjoon no. 11651 (https://www.acmicpc.net/problem/11651)

#include <algorithm>
#include <cstdio>
#include <tuple>
#include <vector>

using std::get;
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
  stable_sort(v.begin(), v.end(),
              [](tuple<int, int> t1, tuple<int, int> t2) -> bool {
                return get<1>(t1) < get<1>(t2);
              });

  for (auto k : v) {
    printf("%d %d\n", get<0>(k), get<1>(k));
  }
}
