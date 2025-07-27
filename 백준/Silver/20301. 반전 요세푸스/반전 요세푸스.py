from collections import deque
N, K, M = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)

cnt = 0
while cnt < K-1:
    tmp = q.popleft()
    q.append(tmp)
    cnt += 1

cnt = 0
dir = 0
answer = []
while q:
    tmp = q.popleft()
    answer.append(tmp)
    cnt += 1
    if cnt % M == 0:
        dir += 1

    if dir % 2 == 0: # 오른쪽 방향
        idx = 0
        while idx < K-1 and q:
            tmp = q.popleft()
            q.append(tmp)
            idx += 1
    else: # 왼쪽 방향
        idx = 0
        while idx < K and q:
            tmp = q.pop()
            q.appendleft(tmp)
            idx += 1
            
for i in range(N):
    print(answer[i])