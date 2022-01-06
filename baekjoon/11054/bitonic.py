# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11054 (https://www.acmicpc.net/problem/11054)

n = int(input())

num = list(map(int, input().split(' ')))
dp1 = [1 for _ in range(n)]
dp2 = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in reversed(range(n-1)):
    for j in reversed(range(i+1, n)):
        if num[i] > num[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
    dp1[i] += dp2[i]

print(max(dp1))
