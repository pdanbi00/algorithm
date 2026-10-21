def solution(balls, share):
    answer = 0
    up = 1
    for i in range(balls, balls - share, -1):
        up *= i
        
    down = 1
    for i in range(1, share+1):
        down *= i
    answer = up // down
    return answer