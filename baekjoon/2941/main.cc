// Copyright 2022 Inhyeok Bang
// Baekjoon no. 2941 (https://www.acmicpc.net/problem/2941)

#include <iostream>

int main() {
  char input[101];
  int i = 0, cnt = 0;

  std::cin >> input;

  while (input[i]) {
    cnt++;
    i++;
    switch (input[i - 1]) {
      case 'c':
        if (input[i] == '=' || input[i] == '-') i++;
        break;
      case 'd':
        if (input[i] == 'z' && input[i + 1] == '=')
          i += 2;
        else if (input[i] == '-')
          i++;
        break;
      case 'l':
        if (input[i] == 'j') i++;
        break;
      case 'n':
        if (input[i] == 'j') i++;
        break;
      case 's':
        if (input[i] == '=') i++;
        break;
      case 'z':
        if (input[i] == '=') i++;
        break;
      default:
        break;
    }
  }

  std::cout << cnt;
}
