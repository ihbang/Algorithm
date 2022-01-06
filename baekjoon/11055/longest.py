# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11055 (https://www.acmicpc.net/problem/11055)

n = int(input())

num = list(map(int, input().split(' ')))
dp = [num[k] for k in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + num[i])

print(max(dp))
