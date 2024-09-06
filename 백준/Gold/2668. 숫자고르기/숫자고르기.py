N = int(input())
graph = [0] * N
result = []

for i in range(N):
    graph[i] = int(input())


def dfs(v, start):
    visited[v] = True
    value = graph[v] - 1
    if not visited[value]:
        dfs(value, start)
    elif visited[value] and value == start:
        result.append(value)

for i in range(N):
    visited = [False] * N
    dfs(i, i)
    
result.sort()
print(len(result))
for r in result:
    print(r+1)