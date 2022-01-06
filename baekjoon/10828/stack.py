# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10828 (https://www.acmicpc.net/problem/10828)

import sys
from operator import itemgetter


class MyStack:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]


N = int(sys.stdin.readline())
s = MyStack()

for i in range(N):
    query = sys.stdin.readline().split(' ')
    if query[0] == 'push':
        s.push(int(query[1]))
    elif query[0] == 'pop\n':
        print(s.pop())
    elif query[0] == 'size\n':
        print(s.size())
    elif query[0] == 'empty\n':
        print(s.empty())
    elif query[0] == 'top\n':
        print(s.top())
