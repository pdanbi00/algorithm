N, K, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

idx = 0
dir = 0
cnt = 0

while arr:
    if dir % 2 == 0:
        idx = (idx + K-1) % len(arr)
    else:
        idx = (idx + (len(arr) - K)) % len(arr)

    print(arr.pop(idx))
    cnt += 1
    if cnt % M == 0:
        dir += 1