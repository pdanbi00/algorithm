from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
dasom = int(input())
hq = []

for _ in range(N-1):
    heappush(hq, -int(input()))

cnt = 0
while hq:
    tmp = heappop(hq)
    tmp = -tmp
    if tmp < dasom:
        break
    tmp -= 1
    dasom += 1
    cnt += 1
    heappush(hq, -tmp)

print(cnt)