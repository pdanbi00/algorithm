import sys
input = sys.stdin.readline

N = int(input())
milk = [int(input()) for _ in range(N)]
milk.sort(reverse=True)
total = 0
for i in range(2, N, 3):
    total += milk[i-2] + milk[i-1]

if N % 3 != 0:
    total += milk[-1]
    if N % 3 == 2:
        total += milk[-2]

print(total)