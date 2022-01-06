# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1158 (https://www.acmicpc.net/problem/1158)

import sys
from collections import deque

N, M = map(int, input().split())
cur = -1

arr = [i+1 for i in range(N)]
d = deque()

while (len(arr) != 0):
    cur = (cur + M) % N
    d.append(str(arr.pop(cur)))
    cur -= 1
    N -= 1

s = '<' + ', '.join(d) + '>'
print(s)
