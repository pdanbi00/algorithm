def solution(n, m):
    answer = []
    min_v = m
    max_v = n
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            max_v = i
            
    if max_v == 1:
        min_v = n * m
    else:
        for i in range(max(n, m), max(n, m) * min(n, m) + 1):
            if i % n == 0 and i % m == 0:
                min_v = i
                break
                
    answer.append(max_v)
    answer.append(min_v)
    return answer