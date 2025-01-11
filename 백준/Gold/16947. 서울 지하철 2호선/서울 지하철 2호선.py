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

# isCycle = [False] * (N+1) # 순환선에 해당하는 역인지 표시
findCycle = False # 순환선 찾았는지 확인
cycle = [] # 순환선에 해당하는 역들

# 사이클 확인하기
def dfs(node, start, tmp):
    global findCycle
    if findCycle:
        return
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, start, tmp+[next_node])
            visited[next_node] = False
        # 순환선일 경우
        elif visited[next_node] and len(tmp) >= 3:
            # 시작한 번호랑 같은 번호가 나오면
            if next_node == start:
                findCycle = True
                # 순환선에 해당하는 역들 다 표시
                for t in tmp:
                    cycle.append(t)
                return

ans = [-1] * (N+1)

def bfs():
    q = deque()

    for c in cycle:
        q.append(c)
        ans[c] = 0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if ans[next_node] == -1:
                q.append(next_node)
                ans[next_node] = ans[node] + 1

for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    dfs(i, i, [i])
    if findCycle:
        break
    visited[i] = False

bfs()

print(" ".join(map(str, ans[1:])))