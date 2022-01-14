// Copyright 2022 Inhyeok Bang
// Baekjoon no. 2941 (https://www.acmicpc.net/problem/2941)

#include <iostream>
#include <vector>

using std::vector;

bool is_prime[10001] = {false};

bool check_prime(int n) {
  if (n == 1) return false;
  if (n == 2) return true;
  for (int i = 2; i < n; i++) {
    if (is_prime[i] && n % i == 0) return false;
  }
  return true;
}

int main() {
  int sum = 0, min = 0;
  int m, n;

  std::cin >> m;
  std::cin >> n;

  for (int i = 1; i < m; i++) {
    is_prime[i] = check_prime(i);
  }
  for (int i = m; i <= n; i++) {
    is_prime[i] = check_prime(i);
    if (is_prime[i]) {
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