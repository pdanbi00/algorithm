def solution(n, computers):
    answer = 0
    def find(a):
        if parents[a] != a:
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parents[b] = a
        else:
            parents[a] = b
            
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)
    for i in range(n):
        find(i)
    p = set(parents)
    
    return len(p)