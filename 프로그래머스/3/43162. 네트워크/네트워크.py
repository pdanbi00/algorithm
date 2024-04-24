def solution(n, computers):
    def dfs(idx):
        visited[idx] = True
        for i in range(n):
            if computers[idx][i] == 1 and visited[i] == False:
                dfs(i)
    answer = 0    
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and not visited[i]:
                dfs(i)
                answer += 1
    
    return answer