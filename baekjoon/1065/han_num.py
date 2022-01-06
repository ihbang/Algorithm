# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1065 (https://www.acmicpc.net/problem/1065)

N = int(input())


def han_num(n):
    if n < 10:
        return n, True
    elif n < 100:
        return n % 10 - int(n / 10), True
    else:
        k = int(n / 10)
        diff, b = han_num(k)
        if b and diff == n % 10 - k % 10:
            return diff, True
        else:
            return 0, False


n = 0
for i in range(1, N + 1):
    _, b = han_num(i)
    if b:
        n += 1

print(n)
