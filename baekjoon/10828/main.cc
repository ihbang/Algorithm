// Copyright 2018 Inhyeok Bang
// Baekjoon no. 10828 (https://www.acmicpc.net/problem/10828)

#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>

class Stack {
 private:
  std::vector<int> items;
  int cur;

 public:
  Stack() : items(10000), cur(-1) {}
  ~Stack() { items.clear(); }

  void push(int x) { items[++cur] = x; }
  int pop() {
    if (this->empty())
      return -1;
    else
      return items[cur--];
  }
  int size() { return cur + 1; }
  int empty() { return this->size() == 0 ? 1 : 0; }
  int top() {
    if (this->empty())
      return -1;
    else
      return items[cur];
  }
};

int main() {
  int n;
  Stack stack;

  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    char str[6];
    scanf("%s", str);
    if (str[0] == 'p') {
      if (str[1] == 'o') {
        printf("%d\n", stack.pop());
      } else {
        int x;
        scanf("%d", &x);
        stack.push(x);
      }
    } else if (str[0] == 's') {
      printf("%d\n", stack.size());
    } else if (str[0] == 'e') {
      printf("%d\n", stack.empty());
    } else if (str[0] == 't') {
      printf("%d\n", stack.top());
    }
  }
}
