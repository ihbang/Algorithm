# Copyright 2018 Inhyeok Bang
# Baekjoon no. 9613 (https://www.acmicpc.net/problem/9613)

def euclidean(a, b):
    if a % b == 0:
        return b
    else:
        return euclidean(b, a % b)


N = int(input())

for i in range(N):
    sum = 0
    num = list(map(int, input().split()))
    for j in range(2, num[0]+1):
        for k in range(1, j):
            if num[j] >= num[k]:
                sum += euclidean(num[j], num[k])
            else:
                sum += euclidean(num[k], num[j])
    print(sum)
