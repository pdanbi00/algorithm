def solution(wallpaper):
    answer = []
    N = len(wallpaper)
    M = len(wallpaper[0])
    lux, luy, rdx, rdy = N, M, 0, 0
    
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i)
                rdy = max(rdy, j)
    answer = [lux, luy, rdx+1, rdy+1]
    return answer