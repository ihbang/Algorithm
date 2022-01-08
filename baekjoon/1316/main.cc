// Copyright 2022 Inhyeok Bang
// Baekjoon no. 1316 (https://www.acmicpc.net/problem/1316)

#include <iostream>

int main() {
  char word[101];
  int num, cnt = 0;

  std::cin >> num;

  for (int i = 0; i < num; i++) {
    int j = 1;
    int alphabets[26] = {0};
    char last_alphabet;

    std::cin >> word;
    last_alphabet = word[0];

    while (word[j]) {
      if (word[j] == last_alphabet) {
        j++;
      } else if (alphabets[last_alphabet - 'a'] == 0) {
        alphabets[last_alphabet - 'a'] = 1;
        last_alphabet = word[j];
        j++;
      } else {
        break;
      }
    }
    if (word[j] == '\0' && alphabets[last_alphabet - 'a'] == 0) cnt++;
  }
  std::cout << cnt;
}
