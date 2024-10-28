N, K = map(int, input().split())
kit = list(map(int, input().split()))
ans = 0
visited = [0] * N
def find(w, n):
    global ans
    if w < 500:
        return
    if n == N:
        ans += 1
        return
    w -= K
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(w+kit[i], n+1)
            visited[i] = 0
find(500, 0)
print(ans)