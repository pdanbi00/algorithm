# A, B, C 각 막대에 놓여진 상태를 합쳐서 큐에 넣고, 딕셔너리로 방문 여부 확인
from collections import deque
arr = [input()[2:] for _ in range(3)]
visited = {}
q = deque()
q.append((arr[0], arr[1], arr[2], 0)) # A막대 상태, B막대 상태, C막대 상태, 움직인 횟수
line = arr[0] + '/' + arr[1] + '/' + arr[2]
visited[line] = 0

while q:
    a, b, c, cnt = q.popleft()
    line = a + '/' + b + '/' + c
    if 'A' not in b and 'A' not in c:
        if 'B' not in a and 'B' not in c:
            if 'C' not in a and 'C' not in b:
                print(cnt)
                exit()

    if len(a) > 0:
        top = a[-1]
        l = a[:-1]
        tmp = l + '/' + b + top + '/' + c
        if tmp not in visited:
            q.append((l, b+top, c, cnt+1))
            visited[tmp] = cnt + 1
        tmp = l + '/' + b + '/' + c + top
        if tmp not in visited:
            q.append((l, b, c + top, cnt + 1))
            visited[tmp] = cnt + 1

    if len(b) > 0:
        top = b[-1]
        l = b[:-1]
        tmp = a + top + '/' + l + '/' + c
        if tmp not in visited:
            q.append((a + top, l, c, cnt+1))
            visited[tmp] = cnt + 1
        tmp = a + '/' + l + '/' + c + top
        if tmp not in visited:
            q.append((a, l, c + top, cnt + 1))
            visited[tmp] = cnt + 1

    if len(c) > 0:
        top = c[-1]
        l = c[:-1]
        tmp = a + top + '/' + b + '/' + l
        if tmp not in visited:
            q.append((a + top, b, l, cnt+1))
            visited[tmp] = cnt + 1
        tmp = a + '/' + b + top + '/' + l
        if tmp not in visited:
            q.append((a, b + top, l, cnt + 1))
            visited[tmp] = cnt + 1