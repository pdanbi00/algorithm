from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

isCycle = [False] * (N+1) # 순환선에 해당하는 역인지 표시
findCycle = False # 순환선 찾았는지 확인

# 사이클 확인하기
def dfs(node, start, idx):
    global findCycle
    if findCycle:
        return
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, start, idx+1)
            visited[next_node] = False
        # 순환선일 경우
        elif visited[next_node] and idx >= 3:
            # 시작한 번호랑 같은 번호가 나오면
            if next_node == start:
                findCycle = True
                # 순환선에 해당하는 역들 다 표시
                for i in range(1, N+1):
                    if visited[i]:
                        isCycle[i] = True
                return

def bfs(idx):
    q = deque()
    visited = [-1] * (N+1)
    q.append(idx)
    visited[idx] = 0
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                if isCycle[next_node]:
                    return visited[node] + 1
                else:
                    q.append(next_node)
                    visited[next_node] = visited[node] + 1

for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    dfs(i, i, 1)
    visited[i] = False

ans = []

for i in range(1, N+1):
    # 순환선에 해당하는 역인지 확인
    if isCycle[i]:
        # 맞으면 0
        ans.append(0)
    else:
        # 아니면 그 역에서부터 bfs로 가장 가까운 순환선 역 찾기
        ans.append(bfs(i))

print(*ans)