from math import sqrt
A, B = map(int, input().split())
a = 1
b = 2 * A
c = B

tmp1 = (-b + int(sqrt(b*b - (4 * c)))) // 2
tmp2 = (-b - int(sqrt(b*b - (4 * c)))) // 2

if tmp1 == tmp2:
    print(tmp1)
else:
    print(min(tmp1, tmp2), max(tmp1, tmp2))