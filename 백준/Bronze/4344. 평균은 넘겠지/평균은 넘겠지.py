T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    avg = (sum(arr[1:]) / arr[0])
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] > avg:
            cnt += 1
    print(f"{(cnt / arr[0]) * 100:.3f}", end="%\n")