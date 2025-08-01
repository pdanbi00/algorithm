from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
router = deque()
while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        router.popleft()
    else:
        if (len(router) < N):
            router.append(num)

if len(router) == 0:
    print("empty")
else:
    while router:
        print(router.popleft(), end = " ")