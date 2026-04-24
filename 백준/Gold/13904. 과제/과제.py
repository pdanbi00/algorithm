from heapq import heappush, heappop

N = int(input())
hq = []
max_day = 0
for _ in range(N):
    d, w = map(int, input().split())
    max_day = max(max_day, d)
    heappush(hq, (-w, d))

visited = [False] * (max_day + 1)
total_score = 0

while hq:
    w, d = heappop(hq)
    w = -w
    # d일부터 1까지 거꾸로 돌면서 비어있는 날 중에 최대한 늦게 배정하기
    for i in range(d, 0, -1):
        if visited[i]:
            continue
        visited[i] = True
        total_score += w
        break

print(total_score)
