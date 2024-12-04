# 핵심 : 총 돌 개수는 고정
#        총 돌의 개수가 3의 배수가 아니라면 어떤 수를 써도 모든 그룹의 돌의 개수를 같게 만들 수는 없음

from collections import deque

def bfs():
    global A, B, C, total, visited
    q = deque()
    q.append((A, B))
    visited[A][B] = True
    while q:
        x, y = q.popleft()
        z = total - x - y
        if x == y == z:
            print(1)
            return
        for A, B in (x, y), (y, z), (z, x):
            # print(A, B)
            if A < B:
                B -= A
                A += A
            elif A > B:
                A -= B
                B += B
            # 두개 개수 같으면 넘어가기
            else:
                continue
            C = total - A - B
            # 제일 작은 값을 X, 제일 큰 값을 Y로 받기
            X = min(A, B, C)
            Y = max(A, B, C)
            if not visited[X][Y]:
                q.append((X, Y))
                visited[X][Y] = True
        # print('-------')
        # print(visited)
    print(0)

# 돌 정보 입력받기
A, B, C = map(int, input().split())

# 전체 돌의 개수
total = A + B + C

# 방문표시
visited = [[False] * (total + 1) for _ in range(total+1)]

# 총 돌의 개수가 3의 배수가 아니면 불가능
if total % 3 != 0:
    print(0)
else:
    bfs()