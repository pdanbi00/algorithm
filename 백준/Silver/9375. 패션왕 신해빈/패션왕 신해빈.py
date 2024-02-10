T = int(input())
for _ in range(T):
    n = int(input())
    cloth = {}
    for i in range(n):
        name, kind = input().split()
        if kind in cloth:
            cloth[kind] += 1
        else:
            cloth[kind] = 1
    ans = 1
    for kind, count in cloth.items():
        ans *= (count + 1)
    print(ans - 1)