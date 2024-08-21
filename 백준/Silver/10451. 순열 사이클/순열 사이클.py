T = int(input())

def dfs(n):
    visited[n] = 1
    for next in graph[n]:
        if visited[next] == 0:
            dfs(next)

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(N):
        graph[i+1].append(nums[i])
    ans = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i] == 0:
            ans += 1
            dfs(i)
    print(ans)

'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''