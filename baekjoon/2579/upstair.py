# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2579 (https://www.acmicpc.net/problem/2579)

n = int(input())

score = [int(input()) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = [0, score[0], score[0]]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + score[i]
    dp[i][2] = dp[i-1][1] + score[i]

print(max(dp[n-1][1], dp[n-1][2]))
