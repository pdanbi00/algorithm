from math import sqrt
def solution(n, k):
    answer = 0
    # k 진수로 바꾸고 이걸 문자열로 바꿔서 0을 기준으로 split
    # 그 수들을 int로 형 변환을 해서 소수인지 판별
    
    # 1. n을 k진수로 변환
    num = ''
    while n > 0:
        tmp = str(n % k)
        num = tmp + num
        n //= k
    arr = num.split("0")
    for a in arr:
        if a != '':
            number = int(a)
            if number == 1:
                continue
            print(number)
            prime = True
            for i in range(2, int(sqrt(number))+1):
                if number % i == 0:
                    prime = False
                    break
                    
            if prime:
                answer += 1
    '''
    11 1
    5 1
    2 0
    1
    '''
    return answer