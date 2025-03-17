# 크루스칼
import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
locations = [list(map(int, input().split())) for _ in range(N)]
edges = []
parent = [i for i in range(N+1)]

# 이미 연결되어 있는 간선들
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 가능한 모든 간선 구하기
for i in range(N):
    for j in range(i+1, N):
        if find(i+1) != find(j+1):
            edges.append((math.sqrt((locations[i][0] - locations[j][0]) ** 2 + (locations[i][1] - locations[j][1]) ** 2), i+1, j+1))
# 간선 비용 기준 오름차순 정렬
edges.sort()
ans = 0

for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += w

print("{:.2f}".format(ans))