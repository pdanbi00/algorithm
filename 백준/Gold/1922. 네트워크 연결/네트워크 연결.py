def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N+1)]


for i in range(M):
    a, b, price = map(int, input().split())
    # 가중치를 오름차순으로 정렬하기 위해 가중치를 첫번째 원소로
    edges.append((price, a, b))
edges.sort()

ans = 0

for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않는 경우에만 포함시킴
    if find(a) != find(b):
        union(a, b)
        ans += cost
print(ans)
