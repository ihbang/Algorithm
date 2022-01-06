# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2751 (https://www.acmicpc.net/problem/2751)

import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

num.sort()
for i in range(N):
    print(num[i])
