def solution(a, b, n):
    answer = 0
    while n >= a:
        new = n // a
        answer += new * b
        
        n -= new * a
        n += new * b
    return answer