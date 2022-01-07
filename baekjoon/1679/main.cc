// Copyright 2021 Inhyeok Bang
// Baekjoon no. 1679 (https://www.acmicpc.net/problem/1679)

#include <iostream>
#include <vector>

std::vector<int> result{0};

int main() {
  int *num;
  int cur;
  int i, j, k;
  int max;
  int step_tot;

  std::cin >> k;
  num = new int(k);
  cur = 0;

  for (i = 0; i < k; i++) std::cin >> num[i];
  std::cin >> max;

  for (j = 1;; j++) {
    for (i = cur; i < k && num[i] <= j; i++) {
    }
    cur = i - 1;
    step_tot = result[j % num[cur]] + j / num[cur];
    if (step_tot <= max)
      result.push_back(step_tot);
    else
      break;
  }

  if (j % 2)
    std::cout << "jjaksoon win at " << j;
  else
    std::cout << "holsoon win at " << j;
}
