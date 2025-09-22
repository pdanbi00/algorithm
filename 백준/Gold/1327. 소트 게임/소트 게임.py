from collections import deque
N, K = map(int, input().split())

nums = tuple(map(int, (input().split())))
target = tuple(range(1, N+1))

visited = set(nums)
q = deque()
q.append((nums, 0))

answer = -1

while q:
    now, cnt = q.popleft()
    if now == target:
        answer = cnt
        break

    for i in range(N - K + 1):
        tmp = now[i:i + K]
        new = now[:i] + tmp[::-1] + now[i + K:]
        if new not in visited:
            q.append((new, cnt+1))
            visited.add(new)

print(answer)