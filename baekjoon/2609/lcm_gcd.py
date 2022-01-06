# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2609 (https://www.acmicpc.net/problem/2609)

def euclidean(a, b):
    if a % b == 0:
        return b
    else:
        return euclidean(b, a % b)


A, B = map(int, input().split())

if A >= B:
    gcd = euclidean(A, B)
else:
    gcd = euclidean(B, A)
lcm = A*B // gcd

print(gcd)
print(lcm)
