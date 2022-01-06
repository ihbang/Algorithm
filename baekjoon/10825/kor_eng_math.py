# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10825 (https://www.acmicpc.net/problem/10825)

import sys
from operator import itemgetter

N = int(sys.stdin.readline())
num = []
for i in range(N):
    inp = sys.stdin.readline().split(' ')
    num.append((inp[0], (int)(inp[1]), (int)(inp[2]), (int)(inp[3])))

num = sorted(num, key=itemgetter(0))
num = sorted(num, key=itemgetter(3), reverse=True)
num = sorted(num, key=itemgetter(2))
num = sorted(num, key=itemgetter(1), reverse=True)
for i in range(N):
    print(num[i][0])
