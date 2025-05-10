from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bridges = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    bridges[a].append((b, c))
    bridges[b].append((a, c))

for i in range(1, N+1):
    bridges[i].sort(reverse=True)

s, e = map(int, input().split())

def bfs(mid):
    q = deque()
    visited = [False] * (N+1)
    visited[s] = True
    q.append(s)

    while q:
        now = q.popleft()
        for next_node, cost in bridges[now]:
            if not visited[next_node] and cost >= mid: # 다리의 중량 제한이 현재 옮기는 중량보다 커야 됨.
                visited[next_node] = True
                q.append(next_node)

    if visited[e]:
        return True
    else:
        return False

start = 1
end = 1000000000

ans = 0
while start <= end:
    mid = (start + end) // 2 # 옮길 수 있는 중량의 최댓값

    if bfs(mid):
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)