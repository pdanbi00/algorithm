# 반대로 계산
# B -> A로
# 연산 수를 줄이려면 큰 값을 작게 만들어야 됨.
# 전부 짝수로 만들고 -> 전부 나눠주는걸 반복
N = int(input())
B = list(map(int, input().split()))
ans = 0 # 연산 횟수
while True:
    for i in range(N):
        if B[i] % 2 == 1: # 홀수라면
            B[i] -= 1
            ans += 1
    if sum(B) == 0: # 다 뺐는데 0이면 완성
        break
    for i in range(N):
        B[i] /= 2
    ans += 1

print(ans)