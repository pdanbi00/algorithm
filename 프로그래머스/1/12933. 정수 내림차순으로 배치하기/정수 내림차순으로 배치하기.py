def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append(str(n % 10))
        n //= 10
    answer.sort(reverse=True)
    answer = int(''.join(answer))
    
    return answer