#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
   
m = [1e12 for i in range(101010)]
m[0] = 0
m[1] = 1
m[2] = 2
    
for i in range(3, n+1):
    for j in range(1, i):
        if i - j*j < 0:
            break
        m[i] = min(m[i], m[i-j*j] + 1)

print(m[n])
