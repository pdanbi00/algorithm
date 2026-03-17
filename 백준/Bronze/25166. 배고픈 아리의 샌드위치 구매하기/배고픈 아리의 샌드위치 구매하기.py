S, M = map(int, input().split())
ari = 1 << 10 - 1

if S < 1024:
    print("No thanks")
else:
    if (S - 1023) & M == (S - 1023):
        print("Thanks")
    else:
        print("Impossible")