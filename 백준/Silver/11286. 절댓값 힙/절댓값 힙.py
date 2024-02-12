import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))