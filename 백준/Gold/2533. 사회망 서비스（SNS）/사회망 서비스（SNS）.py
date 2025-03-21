# 트리 + dp
# 서브트리의 최적해를 구하는 방식
# 내가 얼리어답터가 아닌 경우 : 내 자식들은 모두 얼리어답터여야 됨.
# dp[현재노드] = dp[자식노드들][얼리어답터인 경우의 최적해]
# 내가 얼리어답터인 경우 : 내 자식들은 얼리어답터여도 되고, 아니어도 됨.
# dp[현재노드] = Min(dp[자식노드들][얼리어답터인 경우의 최적해], dp[자식노드들][얼리어답터가 아닌 경우의 최적해])


# dp[현재노드][얼리어답터 여부(1, 0)] : 얼리어답터인 경우 1, 아닌 경우 0
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
dp = [[0] * 2 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def dfs(node):
    global visited
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 0:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][1], dp[next][0])
    dp[node][1] += 1

dfs(1)
print(min(dp[1][0], dp[1][1]))