# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11053 (https://www.acmicpc.net/problem/11053)

n = int(input())

num = list(map(int, input().split(' ')))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))