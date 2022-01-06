// Copyright 2018 Inhyeok Bang
// Baekjoon no. 9012 (https://www.acmicpc.net/problem/9012)

#include <cstdio>

int main() {
  int n;
  char s[51];
  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    int cnt = 0;
    scanf("%s", s);

    for (int j = 0; s[j] && cnt >= 0; ++j) {
      if (s[j] == '(')
        cnt++;
      else if (s[j] == ')')
        cnt--;
    }
    if (cnt == 0)
      printf("YES\n");
    else
      printf("NO\n");
  }
}
