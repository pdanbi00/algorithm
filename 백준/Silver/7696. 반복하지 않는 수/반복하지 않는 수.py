from itertools import permutations
arr = []
for k in range(1, 9):
    for perm in permutations('0123456789', k):
        if perm[0] != '0':
            arr.append(int("".join(perm)))
            if len(arr) == 1000000:
                break
    if len(arr) == 1000000:
        break
while True:
    N = int(input())
    if N == 0:
        break
    print(arr[N-1])