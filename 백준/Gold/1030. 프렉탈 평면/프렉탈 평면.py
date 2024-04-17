def check_black(l, r, c):
    if l == 1:
        return 0
    border = l // n
    if border * (n-k) // 2 <= r < border * (n+k) // 2 and border * (n-k) // 2 <= c < border * (n+k) // 2:
        return 1
    return check_black(border, r % border, c % border)

s, n, k, r1, r2, c1, c2 = map(int, input().split())
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(check_black(n**s, i, j), end='')
    print()