N = int(input())

if N == 1:
    print(4)
    print(1, 1, 0, 1)
else:
    ans1 = 0
    ans2 = []
    for i in range(1, N):
        arr = [N]
        arr.append(i)
        while True:
            tmp = arr[-2] - arr[-1]
            if tmp < 0:
                break
            else:
                arr.append(tmp)
        # print(arr)
        if len(arr) > ans1:
            ans1 = len(arr)
            ans2 = arr

    print(ans1)
    print(*ans2)