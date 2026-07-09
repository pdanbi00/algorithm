def solution(n, t, m, p):
    answer = ""
    tmp = ""
    
    num = 0
    while len(tmp) < t * m:
        tmp += convert_to_base(num, n)
        num += 1
        
    for i in range(t):
        answer += tmp[p-1 + (m*i)]
    
    return answer

def convert_to_base(num, base):
    digits = "0123456789ABCDEF"
    if (num == 0):
        return "0"
    
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result