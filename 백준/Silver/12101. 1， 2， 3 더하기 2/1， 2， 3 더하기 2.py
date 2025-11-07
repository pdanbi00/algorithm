from collections import deque
N, K = map(int, input().split())

visited = set()
ans = []
q = deque()
q.append(('1', 1))
q.append(('2', 2))
q.append(('3', 3))

while q:
    line, total = q.popleft()
    if total == N:
        ans.append(line)
        continue

    for i in range(1, 4):
        if total + i <= N and line + str(i) not in visited:
            q.append((line+str(i), total + i))
            visited.add(line + str(i))

ans.sort()

if K > len(ans):
    print(-1)
else:
    arr = ans[K - 1]

    tmp = arr[0]
    for i in range(1, len(arr)):
        tmp += '+' + arr[i]

    print(tmp)