import sys
input = sys.stdin.readline
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    if b % a == 0 and b // a >= 2:
        print(1)
    else:
        print (0)