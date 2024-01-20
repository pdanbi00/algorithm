def prev_perm(perm):
    i = len(perm) - 1
    while i > 0 and perm[i-1] <= perm[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(perm) - 1
    while perm[i-1] <= perm[j]:
        j -= 1
    perm[i-1], perm[j] = perm[j], perm[i-1]

    j = len(perm) - 1
    while i < j:
        perm[i], perm[j] = perm[j], perm[i]
        i += 1
        j -= 1
    return True

N = int(input())
perm = list(map(int, input().split()))

if prev_perm(perm):
    print(' '.join(map(str, perm)))
else:
    print(-1)