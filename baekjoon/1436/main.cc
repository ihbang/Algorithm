// Copyright 2021 Inhyeok Bang
// Baekjoon no. 1436 (https://www.acmicpc.net/problem/1436)

#include <iostream>

bool is_apocalypse(int n) {
  for (int i = n; i >= 666; i /= 10) {
    if ((i - 666) % 1000 == 0) return true;
  }
  return false;
}

int main() {
  int n, cnt;
  int k = 665;

  std::cin >> n;
  cnt = 0;

  while (cnt < n) {
    k++;
    if (is_apocalypse(k)) cnt++;
  }
  std::cout << k;
}
