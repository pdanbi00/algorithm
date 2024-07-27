K, N, M = map(int, input().split())
tmp = K * N - M
if tmp > 0:
    print(tmp)
else:
    print(0)