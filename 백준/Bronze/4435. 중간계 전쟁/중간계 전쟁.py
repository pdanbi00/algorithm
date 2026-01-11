T = int(input())
g = [1, 2, 3, 3, 4, 10]
s = [1, 2, 2, 2, 3, 5, 10]
for tc in range(1, T+1):
    gan = list(map(int, input().split()))
    sau = list(map(int, input().split()))

    gan_total = 0
    sau_total = 0

    for i in range(6):
        gan_total += g[i] * gan[i]

    for i in range(7):
        sau_total += s[i] * sau[i]

    if gan_total > sau_total:
        print(f"Battle {tc}: Good triumphs over Evil")
    elif gan_total < sau_total:
        print(f"Battle {tc}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {tc}: No victor on this battle field")