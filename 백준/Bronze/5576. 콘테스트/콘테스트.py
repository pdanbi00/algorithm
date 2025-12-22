W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]

W.sort()
K.sort()
print(sum(W[7:]), sum(K[7:]))