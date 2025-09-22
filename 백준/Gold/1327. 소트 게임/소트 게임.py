from collections import deque
N, K = map(int, input().split())

nums = list(input().split())
target = sorted(nums)

visited = set("".join(nums))
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
        new_str = "".join(new)
        if new_str not in visited:
            q.append((new, cnt+1))
            visited.add(new_str)

print(answer)