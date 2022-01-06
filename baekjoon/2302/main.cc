// Copyright 2017 Inhyeok Bang
// Baekjoon no. 2302 (https://www.acmicpc.net/problem/2302)

#include <stdio.h>
#include <stdlib.h>

int f[41] = {0};

int fibonacci(int n) {
  if (n == 0) {
    return 1;
  } else if (n == 1) {
    return 1;
  } else if (f[n - 1] == 0) {
    f[n - 1] = fibonacci(n - 1) + fibonacci(n - 2);
    return f[n - 1];
  } else {
    return f[n - 1];
  }
}

int main() {
  int n, m, i;
  int *arr;
  int result;
  int cur1 = 0;
  int cur2;

  scanf("%d", &n);
  scanf("%d", &m);

  result = 1;
  arr = reinterpret_cast<int *>(malloc((m + 1) * sizeof(int)));

  for (i = 0; i < m; ++i) {
    scanf("%d", arr + i);
  }
  arr[m] = n + 1;

  for (i = 0; i < m + 1; ++i) {
    cur2 = arr[i];
    result *= fibonacci(cur2 - cur1 - 1);
    cur1 = cur2;
  }

  printf("%d\n", result);

  free(arr);

  return 0;
}
