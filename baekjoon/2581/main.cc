// Copyright 2022 Inhyeok Bang
// Baekjoon no. 2941 (https://www.acmicpc.net/problem/2941)

#include <iostream>
#include <vector>

using std::vector;

bool is_prime[10001] = {false};

bool check_prime(int n) {
  for (int i = 1; i < n; i++) {
    if (is_prime[i] && n % i == 0) return false;
  }
  return true;
}

int main() {
  int sum = 0, min = 0;
  int m, n;

  std::cin >> m;
  std::cin >> n;

  is_prime[2] = true;
  is_prime[3] = true;

  for (int i = 4; i < m; i++) {
    is_prime[i] = check_prime(i);
  }
  for (int i = m; i <= n; i++) {
    if (check_prime(i)) {
      sum += i;
      if (min == 0) min = i;
    }
  }
  if (sum == 0) {
    std::cout << -1;
  } else {
    std::cout << sum << std::endl;
    std::cout << min << std::endl;
  }
}