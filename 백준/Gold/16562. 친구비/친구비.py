from collections import deque

N, M, K = map(int, input().split())
friend_money = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if friend_money[a] < friend_money[b]:
        parents[b] = a
    else:
        parents[a] = b

parents = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

tmp = 0
for i in range(1, N+1):
    find(i)

for i in range(1, N+1):
    if parents[i] == i:
        tmp += friend_money[i]

if tmp <= K:
    print(tmp)
else:
    print('Oh no')