// Copyright 2021 Inhyeok Bang
// Baekjoon no. 11729 (https://www.acmicpc.net/problem/11729)

#include <iostream>
#include <utility>
#include <vector>

std::vector<std::pair<int, int>> v;

int rest_tower(int sum) {
  switch (sum) {
    case 3:
      return 3;
    case 4:
      return 2;
    case 5:
      return 1;
    default:
      return 0;
  }
}

void hanoi(int n, int from, int to) {
  if (n == 1) {
    v.push_back(std::pair<int, int>(from, to));
  } else {
    hanoi(n - 1, from, rest_tower(from + to));
    v.push_back(std::pair<int, int>(from, to));
    hanoi(n - 1, rest_tower(from + to), to);
  }
}

int main() {
  int n, size;

  std::cin >> n;

  hanoi(n, 1, 3);
  size = v.size();

  std::cout << size << '\n';
  for (int i = 0; i < size; i++) {
    std::pair<int, int> p = v[i];
    std::cout << p.first << ' ' << p.second;
    if (i != size - 1) std::cout << '\n';
  }

  return 0;
}
