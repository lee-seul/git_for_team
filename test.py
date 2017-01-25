# coding: utf-8

from trial_division_02 import is_prime

n = int(input())

for i in range(2, n):
    print(i)
    is_prime(i)
