# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1463 (https://www.acmicpc.net/problem/1463)

T = int(input())
dp = [0 for _ in range(T+1)]

for i in range(2, T+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

print(dp[T])
