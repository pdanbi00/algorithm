import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

a, b, c, d = False, False, False, False
for _ in range(K):
    i, j = map(int, input().split())
    if i % 2 == 1:
        if (i + j) % 2 == 0:
            a = True
        else:
            b = True
    else:
        if (i + j) % 2 == 0:
            c = True
        else:
            d = True

if a and b and c and d:
    print("YES")
else:
    print("NO")