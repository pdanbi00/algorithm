from collections import deque
A, K = map(int, input().split())

visited = set()
q = deque()

q.append((A, 0))
visited.add(A)

while q:
    num, cnt = q.popleft()
    if num == K:
        answer = cnt
        break

    new_num = num * 2
    if new_num <= K:
        if new_num not in visited:
            q.append((new_num, cnt + 1))
            visited.add(new_num)

    new_num = num + 1
    if new_num <= K:
        if new_num not in visited:
            q.append((new_num, cnt+1))
            visited.add(new_num)

print(answer)