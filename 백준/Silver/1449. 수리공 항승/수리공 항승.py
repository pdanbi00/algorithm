N, L = map(int, input().split())
leak = list(map(int, input().split()))

leak.sort()

cnt = 0
idx = 0
tape = -1
while idx < N:
    tape = leak[idx] + L-1
    cnt += 1
    idx += 1
    while idx < N:
        if leak[idx] > tape:
            break
        idx += 1

print(cnt)