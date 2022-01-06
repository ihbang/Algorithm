// Copyright 2018 Inhyeok Bang
// Baekjoon no. 10799 (https://www.acmicpc.net/problem/10799)

#include <cstdio>

int main() {
  int total = 0, cur = 0;
  bool laser = false;
  char c;

  while (true) {
    scanf("%c", &c);
    if (c == '\n') {
      break;
    } else if (c == '(') {
      cur++;
      laser = true;
    } else if (laser) {
      laser = false;
      total += --cur;
    } else {
      laser = false;
      total++;
      cur--;
    }
  }
  printf("%d\n", total);
}
