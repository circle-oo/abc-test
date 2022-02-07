#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
   
list = [1e12 for i in range(101010)]
list[0] = 0
list[1] = 1
list[2] = 2
    
for i in range(3, n+1):
    for j in range(1, i):
        if i - j*j < 0:
            break
        list[i] = min(list[i], list[i-j*j] + 1)

print(list[n])
