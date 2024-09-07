H, W, N, M = map(int, input().split())
r = H // (N+1)
if H % (N+1) > 0:
    r += 1
c = W // (M+1)
if W % (M+1) > 0:
    c += 1
print(r * c)