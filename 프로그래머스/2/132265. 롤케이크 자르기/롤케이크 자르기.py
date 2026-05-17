def solution(topping):
    answer = 0
    N = len(topping)
    a_arr = [0] * 10001
    b_arr = [0] * 10001
    a_set = set()
    b_set = set()
    
    a_arr[topping[0]] = 1
    a_set.add(topping[0])
    for i in range(1, N):
        b_arr[topping[i]] += 1
        b_set.add(topping[i])
    
    if len(a_set) == len(b_set):
        answer += 1
        
    for i in range(1, N-1):
        a_arr[topping[i]] += 1
        a_set.add(topping[i])
        b_arr[topping[i]] -= 1
        if b_arr[topping[i]] == 0:
            b_set.remove(topping[i])
            
        if len(a_set) == len(b_set):
            answer += 1
    
    return answer