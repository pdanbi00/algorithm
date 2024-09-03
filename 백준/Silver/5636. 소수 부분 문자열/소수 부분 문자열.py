# 소수를 미리 다 찾아놓기
# 소수 순회하면서 테스트케이스에 포함되어 있있는지 확인
# 제일 마지막 소수로 출력

# 1. 소수 찾기
prime = []
for i in range(2, 100001):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        prime.append(i)

# 테스트케이스 확인하기
while True:
    line = input()
    if line == '0':
        break
    ans = ''
    for p in prime:
        if str(p) in line:
            ans = p
    print(ans)