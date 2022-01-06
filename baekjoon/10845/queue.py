# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10845 (https://www.acmicpc.net/problem/10845)

import sys
from operator import itemgetter


class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.items.pop(0)

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
q = Queue()

for i in range(N):
    query = sys.stdin.readline().split()
    if query[0] == 'push':
        q.push(int(query[1]))
    elif query[0] == 'pop':
        print(q.pop())
    elif query[0] == 'size':
        print(q.size())
    elif query[0] == 'empty':
        print(q.empty())
    elif query[0] == 'front':
        print(q.front())
    elif query[0] == 'back':
        print(q.back())
