# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11652 (https://www.acmicpc.net/problem/11652)

import sys
from operator import itemgetter

N = int(sys.stdin.readline())
d = dict()

for i in range(N):
    n = int(sys.stdin.readline())
    if n in d:
        d[n] = d[n] + 1
    else:
        d[n] = 1

s = sorted(d.items())
s = sorted(s, key=itemgetter(1), reverse=True)
print(s[0][0])
