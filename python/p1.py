# Solution to Project Euler problem 1
# Copyright (c) Nhut-Nam Le. All rights reserved.

def solution0(number, a, b):
    if number < 0:
        return 0
    return sum([i for i in range(number) if i % a == 0 or i % b == 0])

print(solution0(10000, 3, 5))
    
def solution1(number, a, b):
    return ((number - 1) // a) * (((number - 1) // a) + 1) * a // 2 + ((number - 1) // b) * (((number - 1) // b) + 1) * b // 2 - ((number - 1) // (a*b)) * (((number - 1) // (a*b)) + 1) * (a*b) // 2 

print(solution1(10000, 3, 5))
