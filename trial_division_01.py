# coding: utf-8

def is_prime(num):
    if n < 2:
        return False
    for i in range(2, n):
        if not num % i:
            return False
    return True

n = int(input())
print(is_prime(n))
