# 최소 신장 트리
# 신장 트리 특성 상 연결된 단 하나의 간선만 끊으면
# 2개의 신장트리로 나눌 수 있음.
# -> 가장 긴 간선을 제거하면 됨

import sys
input = sys.stdin.readline

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N, M = map(int, input().split())
edges = []
parents = [i for i in range(N+1)]
for i in range(M):
    v1, v2, cost = map(int, input().split())
    edges.append((v1, v2, cost))

edges.sort(key=lambda x: x[2])
answer = 0
last_edge = 0
for v1, v2, cost in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        answer += cost
        last_edge = cost
print(answer - last_edge)