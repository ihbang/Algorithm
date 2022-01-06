# Copyright 2018 Inhyeok Bang
# Baekjoon no. 10844 (https://www.acmicpc.net/problem/10844)

T = int(input())
dp = [[0 for _ in range(10)] for _ in range(T)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, T):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[T-1]) % 1000000000)
