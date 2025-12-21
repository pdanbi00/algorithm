T = int(input())
for _ in range(T):
    N = int(input())
    alcohol = []
    for _ in range(N):
        name, amount = input().split()
        alcohol.append((int(amount), name))

    alcohol.sort()
    print(alcohol[-1][1])