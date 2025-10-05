N = int(input())

for _ in range(N):
    arr = list(map(int, input().split()))
    T = arr[0]
    nums = arr[1:]
    info = dict()
    for i in range(T):
        if nums[i] not in info:
            info[nums[i]] = 1
        else:
            info[nums[i]] += 1

    find = False
    for k, v in info.items():
        if v > T//2:
            find = True
            print(k)
            break

    if not find:
        print("SYJKGW")