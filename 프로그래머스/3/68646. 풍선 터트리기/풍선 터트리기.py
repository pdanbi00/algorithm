def solution(a):
    answer = 0
    N = len(a)
    
    left = [0] * N
    right = [0] * N
    
    left[0] = a[0]
    for i in range(1, N):
        left[i] = min(left[i-1], a[i])
    
    right[N-1] = a[N-1]
    for i in range(N-2, -1, -1):
        right[i] = min(right[i+1], a[i])
        
    for i in range(N):
        if a[i] == left[i] or a[i] == right[i]:
            answer += 1
    return answer