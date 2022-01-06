# Copyright 2018 Inhyeok Bang
# Baekjoon no. 11656 (https://www.acmicpc.net/problem/11656)

s = input()
l = []

for i in range(len(s)):
    l.append(s[i:])

l.sort()

for k in l:
    print(k)
