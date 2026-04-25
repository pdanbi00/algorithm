N, K = map(int, input().split())

plan = [0] * 101
A = [0] * 101 # 토마토
AA = [0] * 101 ## 토마토 토마토
B = [0] * 101 # 크림
BB = [0] * 101 ## 크림 크림
C = [0] * 101 # 바질
CC = [0] * 101 ## 바질 바질
for _ in range(K):
    x, y = map(int, input().split())
    plan[x] = y

if plan[1] == 1:
    A[1] = 1
elif plan[1] == 2:
    B[1] = 1
elif plan[1] == 3:
    C[1] = 1
else:
    A[1] = B[1] = C[1] = 1

for i in range(2, N+1):
    if plan[i] == 1:
        A[i] = (B[i-1] + BB[i-1] + C[i-1] + CC[i-1]) % 10000
        AA[i] = A[i-1]
    elif plan[i] == 2:
        B[i] = (A[i-1] + AA[i-1] + C[i-1] + CC[i-1]) % 10000
        BB[i] = B[i-1]
    elif plan[i] == 3:
        C[i] = (A[i - 1] + AA[i - 1] + B[i - 1] + BB[i - 1]) % 10000
        CC[i] = C[i - 1]
    else:
        A[i] = (B[i - 1] + BB[i - 1] + C[i - 1] + CC[i - 1]) % 10000
        AA[i] = A[i - 1]
        B[i] = (A[i - 1] + AA[i - 1] + C[i - 1] + CC[i - 1]) % 10000
        BB[i] = B[i - 1]
        C[i] = (A[i - 1] + AA[i - 1] + B[i - 1] + BB[i - 1]) % 10000
        CC[i] = C[i - 1]

print((A[N] + AA[N] + B[N] + BB[N] + C[N] + CC[N]) % 10000)