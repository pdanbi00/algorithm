from collections import deque
V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    node = arr[0]
    for i in range(1, len(arr)-1, 2):
        graph[node].append((arr[i], arr[i+1]))

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (V+1)
    visited[start] = 0

    res = [0, 0] # start로부터 가장 먼 거리에 있는 노드, 거리

    while q:
        node, dist = q.popleft()

        for next_node, next_dist in graph[node]:
            if visited[next_node] == -1:
                calc_dist = dist + next_dist
                q.append((next_node, calc_dist))
                visited[next_node] = calc_dist
                if res[1] < calc_dist:
                    res[0] = next_node
                    res[1] = calc_dist
                    
    return res

node, dist = bfs(1)
print(bfs(node)[1])