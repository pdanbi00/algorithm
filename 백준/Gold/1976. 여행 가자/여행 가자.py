# Union Find
# 특정 정점부터 특정 정점까지 이어져있는지 확인할 수 있다.

# 노드 합치기
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

# 부모 노드 찾기
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

N = int(input())
M = int(input())
parents = [i for i in range(N)]

for i in range(N):
    link = list(map(int, input().split()))
    for j in range(N):
        if link[j] == 1:
            union(i, j)
path = list(map(int, input().split()))
for i in range(M-1):
    if parents[path[i]-1] != parents[path[i+1]-1]:
        print("NO")
        break
else:
    print("YES")