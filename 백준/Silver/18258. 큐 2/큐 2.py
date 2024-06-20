import sys
input = sys.stdin.readline
from collections import deque

q = deque()
N = int(input())
for _ in range(N):
    line = list(input().split())
    if line[0] == 'push':
        q.append(int(line[1]))
    elif line[0] == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(q))
    elif line[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif line[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif line[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
