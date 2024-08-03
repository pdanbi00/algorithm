# 이게 bfs라니..?
# 물을 옮길 수 있는 경우는 6가지
# A->B, A->C, B->A, B->C. C->A, C->B

# A->B 옮기는 물의 양 : A 전체를 다 옮기거나 B 물통 남은 만큼 다 채우기
# C 물통에 남아있는 물의 양 : Z - A - B

from collections import deque

# x, y의 경우의 수 저장
def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        # x : a물통에 담긴 물의 양
        # y : b물통에 담긴 물의 양
        # z : c물통에 담긴 물의 양

        x, y = q.popleft()
        z = c - x - y

        # a 물통이 비어있을 경우 c물통에 담아있는 양을 정답 배열에 저장
        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        pour(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        pour(x-water, y)
        # y -> x
        water = min(y, a-x)
        pour(x+water, y-water)
        # y -> z
        water = min(y, c-z)
        pour(x, y-water)
        # z -> x
        water = min(z, a-x)
        pour(x+water, y)
        # z -> y
        water = min(z, b-y)
        pour(x, y+water)

a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True

answer = []

bfs()

answer.sort()
print(*answer)