# Copyright 2018 Inhyeok Bang
# Baekjoon no. 1978 (https://www.acmicpc.net/problem/1978)

from collections import deque

arr = [i for i in range(2, 1001)]

i = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        if arr[j] % arr[i] == 0:
            del arr[j]
        else:
            j += 1
    i += 1

N = int(input())
num = deque(map(int, input().split()))
cnt = 0
while len(num) != 0:
    if num.pop() in arr:
        cnt += 1
print(cnt)
