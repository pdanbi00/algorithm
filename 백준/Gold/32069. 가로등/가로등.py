from collections import deque
L, N, K = map(int, input().split())

locations = list(map(int, input().split()))

q = deque()
visited = set()
light = dict()
for l in locations:
    q.append(l)
    visited.add(l)
    light[l] = 0
cnt = 0

while q:
    i = q.popleft()
    cnt += 1
    if i - 1 >= 0 and i - 1 not in visited:
        light[i-1] = light[i] + 1
        visited.add(i-1)
        q.append(i-1)

    if i + 1 <= L and i + 1 not in visited:
        light[i+1] = light[i] + 1
        visited.add(i+1)
        q.append(i+1)

    if cnt == K:
        break

light = sorted(light.items(), key=lambda x : x[1])
for i in range(K):
    print(light[i][1])