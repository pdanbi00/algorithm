N  = int(input())
S = list(map(int, input().split()))
visited = [0] * 10000000

def dfs(idx, sum):
    if idx == N:
        return
    sum += S[idx]
    visited[sum] = 1
    dfs(idx+1, sum)
    dfs(idx+1, sum - S[idx])

dfs(0, 0)
# print(visited[1:])
print(visited[1:].index(0) + 1) # 1부터 보는셈이니깐 인덱스 + 1 해야 원래 값