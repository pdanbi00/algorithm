# 테스트케이스마다 계산하는게 아니라
# 미리 다 계산을 해놓고 불러와서 출력
MAX = 1000000 # 문제에 조건으로 주어짐
d = [1] * (MAX+1) # 각 인덱스는 인덱스에 해당하는 숫자의 모든 약수의 합
s = [0] * (MAX+1) # 각 인덱스는 1부터 인덱스에 해당하는 수까지 모든 약수의 합을 더한거

for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        d[i*j] += i # d[3 * 1] += 3 , d[3 * 2] += 3 이런 느낌 you know?
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]

tc = int(input())
ans = []
for _ in range(tc):
    N = int(input())
    ans.append(s[N])
print('\n'.join(map(str,ans))+'\n')