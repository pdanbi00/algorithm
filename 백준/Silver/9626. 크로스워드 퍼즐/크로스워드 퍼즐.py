M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
odd = ['.', '#']
even = ['#', '.']

for i in range(U + M + D):
    if i < U:
        for j in range(L + N + R):
            if i % 2 == 0:
                print(even[j%2], end='')
            else:
                print(odd[j%2], end='')
        print()
    elif i < U+M:
        tmp = input()
        for j in range(L):
            if i % 2 == 0:
                print(even[j%2], end='')
            else:
                print(odd[j%2], end='')
        print(tmp, end='')
        for j in range(L+N, L+N+R):
            if i % 2 == 0:
                print(even[j % 2], end='')
            else:
                print(odd[j % 2], end='')
        print()
    else:
        for j in range(L + N + R):
            if i % 2 == 0:
                print(even[j%2], end='')
            else:
                print(odd[j%2], end='')
        print()