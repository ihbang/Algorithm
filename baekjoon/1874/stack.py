# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1874 (https://www.acmicpc.net/problem/1874)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if self.size() == 0:
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        else:
            return self.stack[-1]


N = int(input())
s = Stack()
l1 = list(range(N, 0, -1))
l2 = []
flag = True
for i in range(N):
    k = int(input())
    t = s.top()

    if k == t:
        s.pop()
        l2.append('-')
    elif k > t:
        while k > s.top():
            s.push(l1.pop())
            l2.append('+')
        s.pop()
        l2.append('-')
    else:
        flag = False
        break

if flag:
    for i in range(len(l2)):
        print(l2[i])
else:
    print('NO')
