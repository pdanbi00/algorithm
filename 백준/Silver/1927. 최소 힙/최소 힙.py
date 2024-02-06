from heapq import heappush, heappop
import sys
input = sys.stdin.readline
li = []
N = int(input())
for _ in range(N):
    n = int(input())
    if n == 0:
        if li:
            print(heappop(li))
        else:
            print(0)
    else:
        heappush(li, n)

