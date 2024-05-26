T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    base = a % 10
    if base == 0: # 1의 자리가 0인 경우(10의 배수)
        print(10)
    elif base == 1 or base == 5 or base == 6:
        print(base)
    elif base == 4 or base == 9:
        if b % 2 == 0:
            print((base**2) % 10)
        else:
            print(base)
    else:
        if b % 4 == 0:
            print(base**4 % 10)
        else:
            print(base**(b%4) % 10)