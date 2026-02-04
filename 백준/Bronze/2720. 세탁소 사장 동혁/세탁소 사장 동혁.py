T = int(input())
for _ in range(T):
    C = int(input())

    a, b, c, d = 0, 0, 0, 0
    a = C // 25
    C -= a * 25

    b = C // 10
    C -= b * 10

    c = C // 5
    C -= c * 5

    d = C // 1
    C -= d

    print(a, b, c, d)