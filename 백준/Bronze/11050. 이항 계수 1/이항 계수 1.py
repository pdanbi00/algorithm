N, K = map(int, input().split())
total = 1
k_total = 1
n_k_total = 1
for i in range(1, N+1):
    total *= i
for i in range(1, K+1):
    k_total *= i
for i in range(1, N-K+1):
    n_k_total *= i
print(total // (k_total*n_k_total))