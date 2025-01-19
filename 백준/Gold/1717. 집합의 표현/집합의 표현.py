# 유니온 파인드
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_parent(x):
    # 루트 노드가 아니라면 루트 노드 찾을때까지
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    calc, a, b = map(int, input().split())
    if calc == 0:
        union(a, b)
    else:
        a_parent = find_parent(a)
        b_parent = find_parent(b)
        if a_parent == b_parent:
            print('YES')
        else:
            print('NO')