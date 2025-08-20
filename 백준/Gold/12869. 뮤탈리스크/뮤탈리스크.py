import sys
sys.setrecursionlimit(10**6)

N = int(input())
SCV = list(map(int, input().split()))
for _ in range(3-N):
    SCV.append(0)

dp = {}

def dfs(a, b, c):
    # 재방문인 경우
    if (a, b, c) in dp:
        return dp[(a, b, c)]

    # 탈출조건
    if (a, b, c) == (0, 0, 0):
        return 0

    answer = min(dfs(max(a - 9, 0), max(b - 3, 0), max(c - 1, 0)),
                 dfs(max(a - 9, 0), max(b - 1, 0), max(c - 3, 0)),
                 dfs(max(a - 3, 0), max(b - 9, 0), max(c - 1, 0)),
                 dfs(max(a - 3, 0), max(b - 1, 0), max(c - 9, 0)),
                 dfs(max(a - 1, 0), max(b - 3, 0), max(c - 9, 0)),
                 dfs(max(a - 1, 0), max(b - 9, 0), max(c - 3, 0))) + 1

    dp[(a, b, c)] = answer
    return answer

print(dfs(*SCV))