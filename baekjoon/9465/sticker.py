# Copyright 2018 Inhyeok Bang
# Baekjoon no. 9465 (https://www.acmicpc.net/problem/9465)

T = int(input())

for i in range(T):
    n = int(input())
    stickers = [list(map(int, input().split(' '))) for _ in range(2)]
    scores = [[0, 0, 0] for _ in range(n+1)]
    for j in range(1, n+1):
        scores[j][0] = max(scores[j-1][1], scores[j-1][2]) + stickers[0][j-1]
        scores[j][1] = max(scores[j-1][0], scores[j-1][2]) + stickers[1][j-1]
        scores[j][2] = max(scores[j-1])

    print(max(scores[n]))
