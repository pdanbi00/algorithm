from collections import deque
def search_puzzle(board, blocks, state):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # game : 1, table : 0일 때 스킵
            if board[i][j] == state_list[state] or visited[i][j]:
                continue
            blocks.append(bfs(i, j, board, visited, state))
    blocks.sort(key = lambda x : len(x), reverse = True)
            
state_list = [1, 0]
def solution(game_board, table):
    global N
    
    N = len(game_board)
    game_blocks, table_blocks = [], []
    
    # 1. 조각 찾기
    search_puzzle(game_board, game_blocks, 0)
    search_puzzle(table, table_blocks, 1)
    
    answer = 0
    
    for empty in game_blocks:
        flag = False
        # 2. 절대 위치 변경
        game_puzzle = cover_puzzle(empty)
        
        for table_block in table_blocks:
            # 이미 empty를 채웠다면
            if flag:
                break
            # 조각의 개수가 더 적으면 볼 필요가 없음
            if len(game_puzzle) > len(table_block):
                continue
            table_puzzle = cover_puzzle(table_block)
            
            for _ in range(4):
                # 3. 회전
                table_puzzle, cnt = rotate(table_puzzle)
                
                if table_puzzle == game_puzzle:
                    answer += cnt
                    table_blocks.remove(table_block)
                    flag = True
                    break
    
    return answer

# 조각을 (0, 0) 기준으로 변환
def cover_puzzle(puzzle):
    r = [i[0] for i in puzzle]
    c = [i[1] for i in puzzle]
    R = max(r) - min(r) + 1
    C = max(c) - min(c) + 1
    temp = [[0] * C for _ in range(R)]
    
    for i, j in puzzle:
        temp[i-min(r)][j-min(c)] = 1
    return temp

# 조각 회전시키기(시계방향 90도)
def rotate(puzzle):
    cnt = 0
    r = len(puzzle)
    c = len(puzzle[0])
    temp = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if puzzle[i][j] == 1:
                cnt += 1
            temp[j][r-i-1] = puzzle[i][j]
            
    return temp, cnt

# 퍼즐 조각 찾기
def bfs(r, c, board, visited, state):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    q = deque()
    q.append((r, c))
    puzzle = [(r, c)]
    visited[r][c] = True
    
    
    while q:
        r, c, = q.popleft()
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == state and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    puzzle.append((nr, nc))
                    
    return puzzle