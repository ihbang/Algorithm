// Copyright 2021 Inhyeok Bang
// Baekjoon no. 7568 (https://www.acmicpc.net/problem/7568)

#include <algorithm>
#include <iostream>

int *weight;
int *height;
int *grade;

int main() {
  int n;

  std::cin >> n;

  weight = new int[n];
  height = new int[n];
  grade = new int[n];

  for (int i = 0; i < n; i++) {
    std::cin >> weight[i] >> height[i];
    grade[i] = 1;
  }

  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (weight[i] > weight[j] && height[i] > height[j])
        grade[j]++;
      else if (weight[i] < weight[j] && height[i] < height[j])
        grade[i]++;
    }
  }

  for (int i = 0; i < n; i++) {
    std::cout << grade[i];
    if (i != n - 1) std::cout << ' ';
  }

  return 0;
}
