def find(v):
    if parents[v] == v :
        return v
    parents[v] = find(parents[v])
    return parents[v]

def union(v1, v2):
    a = find(v1)
    b = find(v2)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
parents = [i for i in range(N+1)]
day = 1

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges = sorted(edges, key=lambda x : x[2])

for v1, v2, c in edges:
    if c != day:
        print(day)
        break

    if find(v1) == find(v2):
        continue
    union(v1, v2)
    day += 1
else:
    print(day)