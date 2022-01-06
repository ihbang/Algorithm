# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2133 (https://www.acmicpc.net/problem/2133)

N = int(input())

dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in [2*j for j in range(1, N//2 + 1)]:
    dp[i] = 3 * dp[i-2]
    for j in [2*k for k in range(2, i//2 + 1)]:
        dp[i] += 2 * dp[i-j]

print(dp[N])
