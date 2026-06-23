from math import sqrt
def solution(n):
    answer = -1
    num = int(sqrt(n))
    if num * num == n:
        answer = (num+1) * (num+1)
    return answer