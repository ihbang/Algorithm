# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1929 (https://www.acmicpc.net/problem/1929)

from collections import deque
from math import *

M, N = map(int, input().split())
arr = [True for _ in range(N+1)]
arr[0], arr[1] = False, False

for i in range(2, floor(sqrt(N+1))+1):
    for j in range(i+1, N+1):
        if arr[j] and j % i == 0:
            arr[j] = False

for i in range(M, N+1):
    if arr[i]:
        print(i)
