dr = [0, 1, 0, -1] # 방향 전환을 계산하기 위해서 우, 하, 좌, 상
dc = [1, 0, -1, 0] # 방향 전환을 계산하기 위해서 우, 하, 좌, 상
ans = 25 * 25 * 600

def solution(board):
    # dfs + dp, 방향 바뀌면 600원 추가, 아니면 100원 추가
    length = len(board)
    dp = [[1e9] * length for _ in range(length)]
    def dfs(r, c, d, cost, n):
        global ans
        # 현재 위치가 최소 비용인지 확인
        if dp[r][c] < cost:
            return
        else:
            dp[r][c] = cost
            
        # 종료조건
        if r == n-1 and c == n-1:
            if cost < ans:
                ans = cost
            return
        
        # 지나온 곳 체크
        board[r][c] = -1
            
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                if (r == 0 and c == 0) or ((d + i) % 2 == 0):
                    dfs(nr, nc, i, cost+100, n)
                else:
                    dfs(nr, nc, i, cost+600, n)
        board[r][c] = 0
    dfs(0, 0, 0, 0, len(board))
    return ans