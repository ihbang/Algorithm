# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11650 (https://www.acmicpc.net/problem/11650)

import sys
from operator import itemgetter

N = int(sys.stdin.readline())
num = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

num = sorted(num, key=itemgetter(1))
num = sorted(num, key=itemgetter(0))
for i in range(N):
    print(num[i][0], end=' ')
    print(num[i][1])
