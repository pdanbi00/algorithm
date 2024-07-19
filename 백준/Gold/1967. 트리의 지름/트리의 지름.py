# 트리의 지름을 구하는 방법
# 1. 시작정점에서 임의의 정점까지의 거리를 구해서 가장 먼 거리를 구함
# 2. 1에서 찾은 가장 먼 거리를 시작 지점으로 해서 다시 한번 가장 긴 거리를 구함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
board = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))

# 모든 노드에 대해서 가중치를 확인한다? 시간 터질거같은데

visited = [-1] * (N+1)
visited[1] = 0

def dfs(idx, total):
    for next_v, next_cost in board[idx]:
        if visited[next_v] == -1:
            visited[next_v] = total + next_cost
            dfs(next_v, total + next_cost)
# 시작정점(1번 노드)에서 임의의 정점까지의 거리를 구하기
dfs(1, 0)

# 시작 정점으로부터 가장 먼 노드 찾기
v = visited.index(max(visited))
visited = [-1] * (N+1)
visited[v] = 0
dfs(v, 0)

print(max(visited))
