# Solution to Project Euler problem 2
# Copyright (c) Nhut-Nam Le. All rights reserved.

def solution(n):
    x, y = (1, 2)
    s = 0
    while x < n + 1:
        if x % 2 == 0:
            s += x
        x, y = (y, x + y)
    return s

print(solution(4000000))
