# Copyright 2018 Inhyeok Bang
# Baekjoon no. 2011 (https://www.acmicpc.net/problem/2011)

crypto = input()
dp = [0 for _ in range(len(crypto) + 2)]
dp[-2:] = [1, 0]

for i in reversed(range(len(crypto))):
    if crypto[i] == '0':
        dp[i] = 0
    elif int(crypto[i:i+2]) > 26:
        dp[i] = dp[i+1]
    else:
        dp[i] = dp[i+1] + dp[i+2]

print(dp[0] % 1000000)
