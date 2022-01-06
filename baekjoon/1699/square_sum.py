# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1699 (https://www.acmicpc.net/problem/1699)

import math

n = int(input())

dp = [100001 for _ in range(n+1)]
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[n])
