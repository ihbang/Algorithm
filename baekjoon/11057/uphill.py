# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11057 (https://www.acmicpc.net/problem/11057)

def partialSum(l, e):
    sum = 0
    for i in range(e+1):
        sum += l[i]
    return sum


T = int(input())
dp = [[1 for _ in range(10)] for _ in range(T)]

for i in range(1, T):
    for j in range(10):
        dp[i][j] = partialSum(dp[i-1], j)

print(sum(dp[T-1]) % 10007)
