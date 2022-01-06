# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10814 (https://www.acmicpc.net/problem/10814)

import sys
from operator import itemgetter

N = int(sys.stdin.readline())
num = []
for i in range(N):
    inp = sys.stdin.readline().split(' ')
    num.append(((int)(inp[0]), inp[1]))

num = sorted(num, key=itemgetter(0))
for i in range(N):
    print(num[i][0], end=' ')
    print(num[i][1], end='')
