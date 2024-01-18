T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    check = False
    while k <  N*M:
        if k % N == y:
            print(k+1)
            check = True
            break
        else:
            k += M
    if check == False:
        print(-1)