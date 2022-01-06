# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2193 (https://www.acmicpc.net/problem/2193)

def partialSum(l, e):
    sum = 0
    for i in range(e+1):
        sum += l[i]
    return sum


T = int(input())
dp = [[0, 1] for _ in range(T)]

for i in range(1, T):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[T-1]))
