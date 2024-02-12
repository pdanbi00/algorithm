from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    q = deque()
    visited = [False] * 10000
    q.append((A, ''))
    visited[A] = True
    while q:
        n, char = q.popleft()
        if n == B:
            print(char)
            break

        d = n * 2 % 10000
        if not visited[d]:
            q.append((d, char+'D'))
            visited[d] = True

        if n == 0:
            s = 9999
        else:
            s = n - 1
        if not visited[s]:
            q.append((s, char+'S'))
            visited[s] = True

        l = n // 1000 + (n % 1000) * 10
        if not visited[l]:
            q.append((l, char+'L'))
            visited[l] = True

        r = (n % 10) * 1000 + (n // 10)
        if not visited[r]:
            q.append((r, char+'R'))
            visited[r] = True