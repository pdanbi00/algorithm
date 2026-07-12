from collections import deque
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def solution(n, k):
    answer = []
    queue = deque([i for i in range(1, n+1)])
    
    while n > 1:
        fac = factorial(n-1)
        num = queue[(k-1)//fac]
        answer.append(num)
        queue.remove(num)
        n -= 1
        k %= fac
    answer.append(queue[-1])
    return answer