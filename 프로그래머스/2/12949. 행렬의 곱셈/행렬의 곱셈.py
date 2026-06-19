def solution(arr1, arr2):
    answer = []
    N = len(arr1)
    M = len(arr2[0])
    for a in range(N):
        arr = []
        for b in range(M):
            tmp = 0
            for i in range(len(arr1[0])):
                tmp += arr1[a][i] * arr2[i][b]
            arr.append(tmp)
        answer.append(arr)
            
    return answer