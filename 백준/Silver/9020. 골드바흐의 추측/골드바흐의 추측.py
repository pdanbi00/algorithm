from math import sqrt
import sys
input = sys.stdin.readline

def isPrime(x):
    if x == 1:
        return False
    for k in range(2, int(sqrt(x)) + 1):
        if x % k == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    num = int(input())
    a, b = num // 2, num // 2

    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
