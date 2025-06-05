from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x : x[1])

answer = 0
heap = []
for i in range(N):
    while heap and heap[0] <= classes[i][1]:
        heappop(heap)
    heappush(heap, classes[i][2])
    answer = max(answer, len(heap))
print(answer)