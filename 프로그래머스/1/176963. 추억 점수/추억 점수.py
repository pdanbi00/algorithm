def solution(name, yearning, photo):
    answer = []
    info = dict()
    N = len(name)
    for i in range(N):
        info[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        total = 0
        for j in range(len(photo[i])):
            if photo[i][j] in info:
                total += info[photo[i][j]]
        answer.append(total)
    return answer