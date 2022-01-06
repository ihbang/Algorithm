# Copyright 2018 Inhyeok Bang
# Baekjoon no. 9012 (https://www.acmicpc.net/problem/9012)

N = int(input())

for i in range(N):
    cnt = 0
    flag = True
    ps = input()
    if len(ps) % 2 == 1:
        print('NO')
        continue
    for c in ps:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
        if cnt < 0:
            flag = False
            break
    if flag and cnt == 0:
        print('YES')
    else:
        print('NO')
