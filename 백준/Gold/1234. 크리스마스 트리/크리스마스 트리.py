
# 백트래킹
from math import factorial
N, R, G, B = map(int, input().split())
RGB = [R, G, B]
answer = 0
c = [(0, 1), (0, 2), (1, 2)]

def combination(x, y):
    return factorial(x) // factorial(y) // factorial(x-y)

def DFS(n, cnt):
    global answer
    if n == N+1:
        answer += cnt
        return
    for i in range(3):
        if RGB[i] >= n:
            RGB[i] -= n
            DFS(n+1, cnt)
            RGB[i] += n

    if n % 2 == 0:
        for i, j in c:
            if RGB[i] >= n // 2 and RGB[j] >= n // 2:
                RGB[i] -= n // 2
                RGB[j] -= n // 2
                DFS(n + 1, cnt * combination(n, n//2))
                RGB[i] += n // 2
                RGB[j] += n // 2

    if n % 3 == 0:
        if RGB[0] >= n // 3 and RGB[1] >= n // 3 and RGB[2] >= n // 3:
            for i in range(3):
                RGB[i] -= n // 3
            DFS(n+1, cnt * combination(n, n//3) * combination(n-(n//3), n//3))
            for i in range(3):
                RGB[i] += n // 3

DFS(1, 1)
print(answer)