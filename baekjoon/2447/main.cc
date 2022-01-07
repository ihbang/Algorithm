// Copyright 2021 Inhyeok Bang
// Baekjoon no. 2447 (https://www.acmicpc.net/problem/2447)

#include <iostream>

bool **canvas;

void star(int n, int off_x, int off_y) {
  if (n == 3) {
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (x != 1 || y != 1) canvas[off_y + y][off_x + x] = true;
      }
    }
  } else {
    int k = n / 3;
    for (int y = 0; y < 3; y++) {
      for (int x = 0; x < 3; x++) {
        if (x != 1 || y != 1) star(k, off_x + x * k, off_y + y * k);
      }
    }
  }
}

int main() {
  int n;

  std::cin >> n;
  canvas = new bool *[n];
  for (int i = 0; i < n; i++) canvas[i] = new bool[n]{false};

  star(n, 0, 0);

  for (int y = 0; y < n; y++) {
    for (int x = 0; x < n; x++) {
      if (canvas[y][x])
        std::cout << '*';
      else
        std::cout << ' ';
    }
    if (y != n - 1) std::cout << '\n';
  }

  return 0;
}
