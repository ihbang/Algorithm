# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2156 (https://www.acmicpc.net/problem/2156)

n = int(input())

wines = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n+1)]
for j in range(1, n+1):
    dp[j][0] = max(dp[j-1])
    dp[j][1] = dp[j-1][0] + wines[j-1]
    dp[j][2] = dp[j-1][1] + wines[j-1]

print(max(dp[n]))
