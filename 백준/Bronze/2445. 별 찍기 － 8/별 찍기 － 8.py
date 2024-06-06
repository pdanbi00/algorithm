N = int(input())
for i in range(1, N+1):
    a = '*' * i + ' ' * (N-i)
    print(a, end='')
    b = ' ' * (N - i) + '*' * i
    print(b)
for i in range(N-1, 0, -1):
    a = '*' * i + ' ' * (N-i)
    print(a, end='')
    b = ' ' * (N - i) + '*' * i
    print(b)
