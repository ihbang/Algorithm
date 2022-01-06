# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2225 (https://www.acmicpc.net/problem/2225)

N, K = map(int, input().split(' '))

dp = [([1] + [0 for _ in range(K-1)]) for _ in range(N+1)]
dp[0] = [1 for _ in range(K)]

for i in range(1, N+1):
    for j in range(1, K):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[N][K-1] % 1000000000)
