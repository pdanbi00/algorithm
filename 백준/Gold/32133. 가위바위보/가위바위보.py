from collections import deque

N, M, K = map(int, input().split())
arr = [input().strip() for _ in range(N)]

possible = False
q = deque()
q.append((0, list(range(N)), []))

while q:
    r, remaining, moves = q.popleft()

    if len(remaining) == 0:
        continue

    if len(remaining) <= K:
        print(r)
        print("".join(moves))
        possible = True
        break

    if r == M:
        continue

    if r < M:
        for move in ['R', 'S', 'P']:
            new_remaining = []
            for i in remaining:
                if (move == 'R' and arr[i][r] == 'P') or (move == 'S' and arr[i][r] == 'R') or (move == 'P' and arr[i][r] == 'S'):
                    new_remaining.append(i)
            q.append((r+1, new_remaining, moves + [move]))

if not possible:
    print(-1)