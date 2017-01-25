# coding: utf-8

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True

#n = int(input())
#print(is_prime(n))
