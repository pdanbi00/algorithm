# bfs로 출발점에서 거리가 1000 이내인 편의점을 가고,
# 편의점 간 거리가 1000 이내인 곳들을 이어서 가다가
# 마지막 편의점에서 페스티벌까지 1000이내이면 happy 아니면 sad
from collections import deque
def bfs():
    q = deque()
    q.append((home[0], home[1]))
    while q:
        x, y = q.popleft()
        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                next_x, next_y = convenience[i][0], convenience[i][1]
                if abs(x - next_x) + abs(y - next_y) <= 1000:
                    q.append((next_x, next_y))
                    visited[i] = 1
    print("sad")
    return


T = int(input())
for _ in range(T):
    n = int(input())
    visited = [0] * (n+1) # 집 제외하고 편의점이랑 페스티벌
    home = list(map(int, input().split()))
    convenience = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))
    bfs()