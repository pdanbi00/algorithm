A, B, C, N = map(int, input().split())
if A % N == 0 or B % N == 0 or C % N == 0:
    print(1)
else:
        possible = False
        for i in range(N // A + 1):
            if A * i > N:
                break
            for j in range(N // B + 1):
                if A * i + B * j > N:
                    break

                for k in range(N // C + 1):
                    tmp = A * i + B * j + C * k
                    if tmp > N:
                        break

                    if tmp == N:
                        possible = True
                        break
                if possible:
                    break
            if possible:
                break

        if possible:
            print(1)
        else:
            print(0)