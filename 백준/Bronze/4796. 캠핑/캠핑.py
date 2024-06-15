cnt = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        exit()
    a = (V // P) * L
    b = (V - ((V//P) * P))
    if b > L:
        b = L
    print(f'Case {cnt}: {a+b}')
    cnt += 1