# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11052 (https://www.acmicpc.net/problem/11052)

N = int(input())

price = list(map(int, input().split(' ')))
dp = [0 for _ in range(N+1)]
max = 0

for i in range(1, N+1):
    for j in range(i):
        if max < price[j] + dp[i-j-1]:
            max = price[j] + dp[i-j-1]
    dp[i] = max

print(dp[N])
