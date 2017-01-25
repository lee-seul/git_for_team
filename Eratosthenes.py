# coding: utf-8

def sieve(num):
    numbers = [0 for _ in range(num+1)]
    for i in range(2, num+1):
        if not numbers[i]:
            n = 2
            while i * n <= num:
                numbers[i*n] = 1
                n += 1
    primes = [x for x in range(2, num+1) if not numbers[x]]
    return primes

