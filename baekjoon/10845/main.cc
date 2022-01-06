// Copyright 2018 Inhyeok Bang
// Baekjoon no. 10845 (https://www.acmicpc.net/problem/10845)

#include <cstdio>
#include <list>

class Stack {
 private:
  std::list<int> items;

 public:
  Stack() {}
  ~Stack() { items.clear(); }

  void push(int x) { items.push_back(x); }
  int pop() {
    if (this->empty()) {
      return -1;
    } else {
      int tmp = items.front();
      items.pop_front();
      return tmp;
    }
  }
  int size() { return items.size(); }
  int empty() { return this->size() == 0 ? 1 : 0; }
  int front() {
    if (this->empty())
      return -1;
    else
      return items.front();
  }
  int back() {
    if (this->empty())
      return -1;
    else
      return items.back();
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
    } else if (str[0] == 'f') {
      printf("%d\n", stack.front());
    } else if (str[0] == 'b') {
      printf("%d\n", stack.back());
    }
  }
}
