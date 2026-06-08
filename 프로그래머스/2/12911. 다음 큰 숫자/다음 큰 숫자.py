def solution(n):
    answer = 0
    num = n + 1
    binary = bin(n)[2:]
    cnt = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            cnt += 1
    while True:
        target = bin(num)[2:]
        one = 0
        for i in range(len(target)):
            if target[i] == '1':
                one += 1
                
        if one == cnt:
            answer = num
            break
            
        num += 1
        
    return answer