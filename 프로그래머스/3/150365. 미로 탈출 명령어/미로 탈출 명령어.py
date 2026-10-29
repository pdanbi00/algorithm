import sys
sys.setrecursionlimit(10**8)
def solution(n, m, x, y, r, c, k):
    answer = []
    dist = abs(r-x) + abs(c-y)
    
    if dist > k or (k-dist) % 2 != 0:
        return "impossible"
    
    # d, l, r, u 순서(아래, 왼, 오, 위)
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    d = ['d', 'l', 'r', 'u']
    
    def dfs(cx, cy, remain):
        if remain == 0:
            if cx == r and cy == c:
                return True
            return False
        
        if abs(cx - r) + abs(cy - c) > remain:
            return False
        for i in range(4):
            nx = cx + dr[i]
            ny = cy + dc[i]
            
            if 0 < nx <= n and 0 < ny <= m:
                answer.append(d[i])
                if dfs(nx, ny, remain - 1):
                    return True
                answer.pop()
        
        return False
    dfs(x, y, k)
    return "".join(answer)