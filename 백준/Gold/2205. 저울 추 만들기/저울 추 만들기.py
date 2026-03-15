# 큰 수 일수록 2의 거듭제곱이 가능한 경우가 별로 없어서 큰 수부터 처리
N = int(input())

check = []
idx = 2
while True:
    if idx <= (2 * N):
        check.append(idx)
    else:
        break
    idx *= 2

weight = [0] * (N+1)
weight[0] = 1

for i in range(N, 0, -1):
    for k in check:
        if k > i and k - i <= N:
            if weight[i] == 0 and weight[k-i] == 0:
                weight[i] = k-i
                weight[k-i] = i

for i in range(1, N+1):
    print(weight[i])