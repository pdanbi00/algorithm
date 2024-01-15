# 에라토스테네스의 체 이용
MAX = 1000000
check = [0] * (MAX + 1)
check[0] = True # True가 소수가 아니라서 지운다는 의미
check[1] = True

for i in range(2, MAX + 1):
    if not check[i]: # 안 지워졌다는건 소수라는거임. 그래서 그 수의 배수들을 싹 지운다.
        j = i + i # i * 2임 i의 배수들 싹 다 지우겠다는거임
        while j <= MAX:
            check[j] = True
            j += i # i 배수를 계속 만든다잉

M, N = map(int, input().split())
for i in range(M, N+1):
    if not check[i]:
        print(i)