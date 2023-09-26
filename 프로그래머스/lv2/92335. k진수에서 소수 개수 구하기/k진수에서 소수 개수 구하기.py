def solution(n, k):
    num = []
    word = ''
    
    # k 진수로 변환
    while n:
        word = str(n % k) + word
        n = n // k
    
    # k 진수로 나타낸 수를 0을 기준으로 잘라내기
    word = word.split('0')
    
    # 정답으로 출력할 소수 개수
    count = 0
    for w in word:
        if len(w) == 0: # 00이 붙어있으면 w는 ''이 됨. 그래서 이거는 패스
            continue
        if int(w) < 2: # 0, 1이면 소수 아님
            continue
        is_prime = True
        for i in range(2, int(int(w) ** 0.5) + 1):
            if int(w) % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
        

    answer = count
    return answer