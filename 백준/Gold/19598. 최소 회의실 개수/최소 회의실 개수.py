from heapq import heappush,heappop
import sys
input = sys.stdin.readline
lessons = []
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    lessons.append((start, end))

lessons.sort()

q = []
answer = 0

for start, end in lessons:
    if q and q[0] <= start:
        heappop(q)
    heappush(q, end)
    answer = max(answer, len(q))

print(answer)