# MST
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

V, E = map(int, input().split())
edges = []
parents = [i for i in range(V+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
ans = 0
for edge in edges:
    weight, a, b = edge
    if find(a) != find(b):
        union(a, b)
        ans += weight
print(ans)