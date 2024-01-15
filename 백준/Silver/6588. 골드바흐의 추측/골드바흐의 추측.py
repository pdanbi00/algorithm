import sys
# 에라토스테네스의 체 이용
MAX = 1000000
check = [0] * (MAX + 1)
check[0] = check[1] = True
prime = [] # 소수들을 담아놓을 리스트
for i in range(2, MAX+1):
    if not check[i]:
        prime.append(i) # 안 지워지고 남아있다는건 소수라는 의미
        j = i + i
        while j <= MAX:
            check[j] = True
            j += i # i 배수들을 다 지우겠다는거임
prime = prime[1:] # 두 홀수 소수의 합으로 나타낼 수 있다고 해놨는데 가장 작은 소수는 2로 짝수라서 제외시키려고
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for p in prime:
        if check[n-p] == False: # 소수들을 작은거부터 찾아가니깐 소수a + 소수b = n인지 찾는거니깐 소수 리스트에서 하나 뽑고, n에서 그 수 뺀거도 소수인지 확인하는거임
            # print(f'{n} = {p} + {n-p}')
            print("{0} = {1} + {2}".format(n, p, n-p))
            break
