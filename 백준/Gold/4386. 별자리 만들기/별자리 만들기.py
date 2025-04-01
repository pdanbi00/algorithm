# 최소신장트리 MST - 크루스칼
from math import sqrt

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

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]

ans = 0

edges = []
parent = [i for i in range(N)]

for i in range(N):
    for j in range(i+1, N):
        dis = sqrt((abs(stars[i][0] - stars[j][0]) ** 2) + (abs(stars[i][1] - stars[j][1]) ** 2))
        edges.append((dis, i, j))

edges.sort()

for edge in edges:
    cost, n1, n2 = edge[0], edge[1], edge[2]
    if find(n1) != find(n2):
        union(n1, n2)
        ans += cost
        
print(round(ans, 2))