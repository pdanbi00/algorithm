# import sys
# input = sys.stdin.readline
# BFS라니
from collections import deque
A, B = map(int, input().split())
# graph = [-1] * (B+1) # 이렇게 배열 만들면 B가 10^9라서 메모리 초과 남. bfs 큐에서 연산 횟수 주고 받게 해야 됨.
q = deque()
q.append((A, 1))
while q:
    now, cnt = q.popleft()
    if now == B:
        print(cnt)
        break
    if now * 2 <= B:
        q.append((now*2, cnt+1))
    n = int(str(now)+'1')
    if n <= B:
        q.append((n, cnt+1))
else:
    print(-1)