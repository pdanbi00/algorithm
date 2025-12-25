import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

K = int(input())
destroyed = list(map(int, input().split()))

answer = []
visited = set()
for d in destroyed:
    possible = True
    for next_d in graph[d]:
        if next_d not in destroyed:
            possible = False
            break
    if possible:
        answer.append(d)
        visited.add(d)
        for next_d in graph[d]:
            visited.add(next_d)

if len(visited) == len(destroyed):
    print(len(answer))
    print(*answer)
else:
    print(-1)