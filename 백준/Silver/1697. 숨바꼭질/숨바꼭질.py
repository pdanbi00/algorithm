# 이건 시간 터짐

# def solve(n, k, cnt):
#     global min_v
#     if cnt > min_v:
#         return
#     if n == k:
#         min_v = min(min_v, cnt)
#         return
#     else:
#         if n + 1 <= 100000:
#             solve(n+1, k, cnt+1)
#         if n - 1 >= 0:
#             solve(n-1, k, cnt+1)
#         if 0 <= n * 2 <= 100000:
#             solve(n*2, k, cnt+1)
#
# N, K = map(int, input().split())
# min_v = 100000
# solve(N, K, 0)
# print(min_v)

def bfs(n, k):
    stack = []
    visited = [0] * 100001
    cnt = 0
    stack.append((n, cnt))
    visited[n] = 1
    while stack:
        x, xcnt = stack.pop(0)
        xcnt += 1
        for nx in ((x+1), (x-1), (x*2)):
            if 0 <= nx <= 100000 and not visited[nx]:
                if nx == k:
                    return print(xcnt)
                else:
                    stack.append((nx, xcnt))
                    visited[nx] = 1



N, K = map(int, input().split())
bfs(N, K)
if N == K:
    print(0)