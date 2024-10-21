# 출력 초과...
N, a, b = map(int, input().split())
if a >= b:
    ga = [i for i in range(1, a+1)]
    dan = [i for i in range(b-1, 0, -1)]
else:
    ga = [i for i in range(1, a)]
    dan = [i for i in range(b, 0, -1)]
tmp = ga + dan
if len(tmp) > N:
    print(-1)
else:
    if a + b <= N:
        print(tmp[0], end = " ")
        for i in range(N - (a + b-1)):
            print(1, end = " ")
        for i in range(1, len(tmp)):
            print(tmp[i], end = ' ')
    else:
        for i in range(len(tmp)):
            print(tmp[i], end = " ")