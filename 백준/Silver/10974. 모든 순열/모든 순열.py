def perm(index, p):
    if index == N:
        print(' '.join(map(str, p)))
    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            perm(index+1, p+[i])
            used[i] = False

N = int(input())
used = [0] * (N+1)
perm(0, [])