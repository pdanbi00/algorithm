def solution(mats, park):
    answer = 0
    N = len(park)
    M = len(park[0])
    
    for i in range(N):
        for j in range(M):
            if park[i][j] == "-1":
                park[i][j] = 1
            else:
                park[i][j] = 0
                
    for i in range(N):
        for j in range(M):
            if park[i][j] == 1:
                if i-1 >= 0 and j-1 >= 0:
                    park[i][j] += min(park[i-1][j], park[i][j-1], park[i-1][j-1])
                    answer = max(answer, park[i][j])
                    
    tmp = -1
    for mat in mats:
        if mat <= answer:
            tmp = max(tmp, mat)
    return tmp