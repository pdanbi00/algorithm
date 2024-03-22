# Union Find 알고리즘이다...
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
parents = [i for i in range(n)]

# 부모 노드 찾아주기
def find(x):
    while x != parents[x]:
        x = parents[x]
    return x

def union(x1, x2):
    parents_x1 = find(x1)
    parents_x2 = find(x2)
    if parents_x1 < parents_x2:
        parents[parents_x2] = parents_x1
    else:
        parents[parents_x1] = parents_x2

result = 0
for i in range(m):
    v1, v2 = map(int, input().split())
    if find(v1) == find(v2):
        result = i+1
        break
    union(v1, v2)
print(result)