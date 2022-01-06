// Copyright 2018 Inhyeok Bang
// Baekjoon no. 11052 (https://www.acmicpc.net/problem/11052)

#include <iostream>
#include <string>
#include <vector>

using std::vector;

vector<int> price;
vector<int> dp;

int buyCard(int k) {
  if (dp[k] != -1) {
    return dp[k];
  } else {
    int m = 0;
    for (int i = 1; i <= k; ++i) {
      int tmp = buyCard(k - i) + price[i];
      if (m < tmp) m = tmp;
    }
    dp[k] = m;
    return dp[k];
  }
}

int main() {
  int n;
  std::cin >> n;

  dp.push_back(0);
  price.push_back(0);
  for (int i = 0; i < n; ++i) {
    int p;
    std::cin >> p;
    price.push_back(p);
    dp.push_back(-1);
  }
  std::cout << buyCard(n) << std::endl;
}
