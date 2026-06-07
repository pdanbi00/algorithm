import math
def check(num):
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True

def solution(n):
    answer = n-1
    for i in range(2, n+1):
        if check(i):
            answer -= 1
    return answer