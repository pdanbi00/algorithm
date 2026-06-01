def solution(elements):
    answer = 0
    arr = []
    N = len(elements)
    for i in range(N*2-1):
        arr.append(elements[i%N])
        
    S = set()
    
    for i in range(1, N+1):
        tmp = sum(arr[:i])
        S.add(tmp)
        
        for j in range(i, N*2-1):
            tmp += arr[j]
            tmp -= arr[j-i]
            S.add(tmp)
            
    return len(S)