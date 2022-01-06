# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10866 (https://www.acmicpc.net/problem/10866)

import sys
from operator import itemgetter


class Deque:
    def __init__(self):
        self.items = []

    def push_front(self, n):
        self.items.insert(0, n)

    def push_back(self, n):
        self.items.append(n)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.items.pop(0)

    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        if self.empty():
            return -1
        else:
            return self.items[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.items[-1]


N = int(sys.stdin.readline())
q = Deque()

for i in range(N):
    query = sys.stdin.readline().split()
    if query[0] == 'push_front':
        q.push_front(int(query[1]))
    elif query[0] == 'push_back':
        q.push_back(int(query[1]))
    elif query[0] == 'pop_front':
        print(q.pop_front())
    elif query[0] == 'pop_back':
        print(q.pop_back())
    elif query[0] == 'size':
        print(q.size())
    elif query[0] == 'empty':
        print(q.empty())
    elif query[0] == 'front':
        print(q.front())
    elif query[0] == 'back':
        print(q.back())
