# 2차원 배열 bfs
from collections import deque
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(visited):
    global ans
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    while q:
        cur_r, cur_c = q.popleft()
        for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < h+2 and 0 <= nc < w+2 and visited[nr][nc] == False and board[nr][nc] != '*':
                # 열쇠인 경우(소문자)
                if board[nr][nc] in small:
                    if board[nr][nc] not in key: # 기존에 없던 키라면
                        key[board[nr][nc]] = True # 키 추가하기
                        # 새로운 열쇠 찾으면 새로 탐색하기 위해서 visited 초기화
                        visited = [[False] * (w+2) for _ in range(h+2)]
                # 문인 경우(대문자)
                elif board[nr][nc] in big:
                    # 문에 해당하는 열쇠가 없을 경우 통과
                    tmp = board[nr][nc].lower()
                    if tmp not in key:
                        continue
                # 문서인 경우($) 전에 방문한 적 없는 위치여야 됨.(중복 카운팅 없애기 위해서)
                elif board[nr][nc] == '$' and (nr, nc) not in visited_doc:
                    ans += 1
                    visited_doc.append((nr, nc)) # 해당 위치는 다시 방문하면 안되기 때문에 저장
                visited[nr][nc] = True
                q.append((nr, nc))

T = int(input())
for tc in range(T):
    h, w = map(int, input().split())
    # 처음부터 바로 확인할 수 있도록 빈공간으로 감싸주기
    board = ['.' + input() + '.' for _ in range(h)]
    board = ['.' * (w+2)] + board + ['.' * (w+2)]
    visited = [[False] * (w+2) for _ in range(h+2)]
    key = {} # 갖고 있는 키 저장
    visited_doc = [] # 방문한 문서 위치 저장
    haveKey = input()
    for hk in haveKey:
        if hk.isalpha(): # 만약 알파벳이라면
            key[hk] = True # 키로 저장

    ans = 0
    bfs(visited)
    print(ans)
