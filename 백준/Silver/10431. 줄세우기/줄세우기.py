P = int(input())
for _ in range(P):
    T, *nums = map(int, input().split())
    ans = 0
    arr = []
    for i in range(len(nums)):
        if i == 0:
            arr.append(nums[i])
            continue
        now = nums[i]
        if now > max(arr):
            arr.append(now)
            continue

        for j in range(len(arr)):
            if arr[j] > now:
                ans += len(arr) - j
                arr.insert(j, now)
                break
    print(T, ans)