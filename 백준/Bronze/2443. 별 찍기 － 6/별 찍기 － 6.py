N = int(input())
for i in range(N):
    print(' ' * i, end='')
    print('*' * (2*N - (i*2 + 1)), end='')
    print(' ')