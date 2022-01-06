# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1406 (https://www.acmicpc.net/problem/1406)

import sys
from collections import deque

s = input()
ldq = deque(s)
rdq = deque()
N = int(input())

for i in range(N):
    q = sys.stdin.readline().split()
    if q[0] == 'L':
        if len(ldq) != 0:
            rdq.appendleft(ldq.pop())
    elif q[0] == 'D':
        if len(rdq) != 0:
            ldq.append(rdq.popleft())
    elif q[0] == 'B':
        if len(ldq) != 0:
            ldq.pop()
    elif q[0] == 'P':
        ldq.append(q[1])

print(''.join(ldq + rdq))
