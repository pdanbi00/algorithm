# bfs
def check(now):
    ans = []
    # 뒤에서부터 경로 찾기
    temp = now
    for _ in range(visited[now]):
        ans.append(temp)
        temp = move[temp]
    # 뒤집어서 출력
    print(' '.join(map(str, ans[::-1])))
from collections import deque
N, K = map(int, input().split())
visited = [0]*100001 # 방문 여부 표시. 걸린 시간 표시
move = [0] * 100001 # 이전에 어디서부터 온 건지 표시
q = deque()
q.append(N)
visited[N] = 1

while q:
    now = q.popleft()
    if now == K:
        print(visited[now]-1)
        check(now)
        break
    if now * 2 <= 100000 and visited[now * 2] == 0:
        q.append(now*2)
        visited[now*2] = visited[now] + 1
        move[now*2] = now
    if now + 1 <= 100000 and visited[now + 1] == 0:
        q.append(now+1)
        visited[now+1] = visited[now] + 1
        move[now + 1] = now
    if now - 1 >= 0 and visited[now - 1] == 0:
        q.append(now-1)
        visited[now-1] = visited[now] + 1
        move[now - 1] = now
