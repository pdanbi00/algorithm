from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -x)
