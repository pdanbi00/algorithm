import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

K = int(input())
destroyed = list(map(int, input().split()))
destroyed.sort()

is_destroyed = [False] * (N+1)
for d in destroyed:
    is_destroyed[d] = True
result = []

for d in destroyed:
    for j in graph[d]:
        if is_destroyed[j] == False:
            break
    else:
        result.append(d)

if len(result) == 0:
    print(-1)

else:
    check = set()
    for i in result:
        check.add(i)
        for j in graph[i]:
            check.add(j)
    check = sorted(list(check))
    if len(check) != K:
        print(-1)
    else:
        for i in range(K):
            if check[i] != destroyed[i]:
                print(-1)
                break
        else:
            result.sort()
            print(len(result))
            print(*result)