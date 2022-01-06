# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1003 (https://www.acmicpc.net/problem/1003)

memo = [(1, 0), (0, 1)] + [0] * 39


def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])


def fibonacci(n):
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = add_pair(fibonacci(n-1), fibonacci(n-2))
        return memo[n]


N = int(input())

for i in range(N):
    n = int(input())
    p = fibonacci(n)
    print('%d %d' % p)
