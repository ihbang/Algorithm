# Copyright 2018 Inhyeok Bang
# Baekjoon no. 9461 (https://www.acmicpc.net/problem/9461)

T = int(input())

maxN = 100
dp = [0 for _ in range(maxN)]
dp[0:5] = [1, 1, 1, 2, 2]

for i in range(5, maxN):
    dp[i] = dp[i-1] + dp[i-5]

for i in [int(input()) for _ in range(T)]:
    print(dp[i-1])
