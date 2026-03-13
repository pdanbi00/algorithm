from collections import deque
N, M = map(int, input().split())
yard = [0] + list(map(int, input().split()))

answer = 1
visited = set()

q = deque()
q.append((0, 0, 1))
visited.add((0, 0, 1))
dx = [1, 2]
while q:
    idx, time, size = q.popleft()
    if time == M or idx >= N:
        answer = max(answer, size)
        continue

    # 굴리기
    n_idx = idx + 1
    if n_idx <= N:
        tmp_size = size + yard[n_idx]
        if (n_idx, time+1, tmp_size) not in visited:
            q.append((n_idx, time+1, tmp_size))
            visited.add((n_idx, time+1, tmp_size))

    # 던지기
    n_idx = idx + 2
    if n_idx <= N:
        tmp_size = (size // 2) + yard[n_idx]
        if (n_idx, time+1, tmp_size) not in visited:
            q.append((n_idx, time+1, tmp_size))
            visited.add((n_idx, time+1, tmp_size))

print(answer)