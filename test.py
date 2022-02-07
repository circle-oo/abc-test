#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
   
dp = [1e12 for i in range(101010)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
    
for i in range(3, n+1):
    for j in range(1, i):
        if i - j*j < 0:
            break
        dp[i] = min(dp[i], dp[i-j*j] + 1)

print(dp[n])
