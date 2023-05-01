N = int(input())
arr = [0] * (N+1)
if N >= 2:
    arr[2] = 1
    if N >= 3:
        arr[3] = 1
        if N >= 4:
            for i in range(4, N+1):
                if i % 3 != 0 and i % 2 != 0:
                    arr[i] = arr[i-1] + 1
                elif i % 3 == 0 and i % 2 != 0:
                    arr[i] = min(arr[i-1], arr[i//3]) + 1
                elif i % 3 != 0 and i % 2 == 0:
                    arr[i] = min(arr[i-1], arr[i//2]) + 1
                elif i % 3 == 0 and i % 2 == 0:
                    arr[i] = min(arr[i - 1], arr[i // 2], arr[i // 3]) + 1

print(arr[N])