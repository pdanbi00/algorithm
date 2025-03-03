# 골드바흐의 추측에 따르면 4 이상의 모든 짝수는 소수 + 소수가 가능함
from math import sqrt
import sys
input = sys.stdin.readline

p = [1, 1] + [0] * 1999999
for i in range(2, int(sqrt(2000000))+1):
    j = 2
    while i * j <= 2000000:
        p[i*j] = 1
        j += 1
prime = set()
for i in range(2, 2000001):
    if p[i] == 0:
        prime.add(i)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    tmp = a + b
    possible = True
    if tmp <= 3:
        print("NO")
    else:
        # 골드바흐의 추측에 의해서 짝수면 YES
        if tmp % 2 == 0:
            print("YES")
        else:
            if tmp - 2 > 2000000:
                for i in prime:
                    if (tmp - 2) % i == 0:
                        print("NO")
                        possible = False
                        break
                if possible:
                    print("YES")
            else:
                if tmp - 2 in prime:
                    print("YES")
                else:
                    print("NO")