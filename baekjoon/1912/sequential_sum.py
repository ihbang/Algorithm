# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1912 (https://www.acmicpc.net/problem/1912)

n = int(input())

num = list(map(int, input().split(' ')))
for i in range(1, n):
    if num[i-1] > 0:
        num[i] += num[i-1]

print(max(num))
