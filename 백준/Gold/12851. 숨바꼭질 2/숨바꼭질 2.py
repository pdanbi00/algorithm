from collections import deque
N, K = map(int, input().split())
visited = [-1] * 200001
q = deque()

cnt = 0
min_time = 100001
q.append(N)
visited[N] = 0

while q:
    now = q.popleft()
    if visited[now] > min_time:
        break
    if now == K:
        if min_time == 100001:
            min_time = visited[now]

        if visited[now] == min_time:
            cnt += 1
        continue

    arr = [now - 1, now + 1, now * 2]
    for a in arr:
        if 0 <= a < 200001 and (visited[a] == -1 or visited[a] >= visited[now] + 1):
            visited[a] = visited[now] + 1
            q.append(a)

print(min_time)
print(cnt)