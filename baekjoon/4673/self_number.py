# Copyright 2018 Inhyeok Bang
# Baekjoon no. 4673 (https://www.acmicpc.net/problem/4673)

nlist = [True] * 10000


def sum_cipher(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_cipher(int(n / 10))


def self_num(n):
    return n + sum_cipher(n)


def self_nums():
    for i in range(10000):
        k = self_num(i)
        if k <= 10000:
            nlist[k - 1] = False
        else:
            continue


self_nums()
for i in range(10000):
    if nlist[i]:
        print(i + 1)
