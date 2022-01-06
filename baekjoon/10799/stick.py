# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10799 (https://www.acmicpc.net/problem/10799)

import sys
from operator import itemgetter

s = sys.stdin.readline()
cnt = 0
pieces = 0
flag = False

for i in range(len(s)-1):
    k = s[i]
    if k == '(':
        cnt += 1
        flag = True
    elif flag:
        cnt -= 1
        pieces += cnt
        flag = False
    else:
        cnt -= 1
        pieces += 1
        flag = False

print(pieces)
