from collections import deque
N, M = map(int, input().split())
banned = set()

for _ in range(M):
    num = int(input())
    banned.add(num)

q = deque()
checked = set() # 돌 번호, 점프 속도

if 2 in banned:
    print(-1)
else:
    q.append((2, 1, 1)) # 돌 번호, 점프 속도, 점프 횟수
    checked.add((2, 1))

    answer = -1
    while q:
        idx, jump, cnt = q.popleft()
        if idx == N:
            answer = cnt
            break

        for k in (-1, 0, 1):
            new_jump = jump + k
            if new_jump > 0:
                n_idx = idx + new_jump
                if n_idx <= N and n_idx not in banned and (n_idx, new_jump) not in checked:
                    q.append((n_idx, new_jump, cnt+1))
                    checked.add((n_idx, new_jump))

    print(answer)