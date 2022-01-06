// Copyright 2021 Inhyeok Bang
// Baekjoon no. 1018 (https://www.acmicpc.net/problem/1018)

#include <algorithm>
#include <iostream>

using std::cin;
using std::cout;
using std::min;

bool **board;
int **min_paint;

int make_chessboard(int x, int y) {
  int cnt = 0;
  bool correct_color = board[y][x];

  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      if (correct_color != board[i + y][j + x]) cnt++;
      correct_color = !correct_color;
    }
    correct_color = !correct_color;
  }
  return min(cnt, 64 - cnt);
}

int main() {
  int m, n;
  int min, tmp;
  char *row;

  cin >> n >> m;
  min = m * n;
  row = new char[m];
  board = new bool *[n];
  for (int i = 0; i < n; i++) board[i] = new bool[m];
  min_paint = new int *[n - 7];
  for (int i = 0; i < n - 7; i++) min_paint[i] = new int[m - 7];

  for (int i = 0; i < n; i++) {
    cin >> row;
    for (int j = 0; j < m; j++) {
      board[i][j] = (row[j] == 'B');
    }
  }

  for (int i = 0; i < n - 7; i++) {
    for (int j = 0; j < m - 7; j++) {
      tmp = make_chessboard(j, i);
      if (tmp < min) min = tmp;
    }
  }
  cout << min;
  return 0;
}
