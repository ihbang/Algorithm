# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11004 (https://www.acmicpc.net/problem/11004)

import sys
from operator import itemgetter

N, K = map(int, sys.stdin.readline().split(' '))
num = list(map(int, sys.stdin.readline().split(' ')))

num.sort()
print(num[K-1])
