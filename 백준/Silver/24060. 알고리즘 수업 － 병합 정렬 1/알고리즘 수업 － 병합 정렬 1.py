def merge(nums, s, q, e):
    global cnt, result
    i = s
    j = q+1
    t = 0
    tmp = [0] * (e-s+1)
    while (i <= q and j <= e):
        if (nums[i] <= nums[j]):
            tmp[t] = nums[i]
            t += 1
            i += 1
        else:
            tmp[t] = nums[j]
            t += 1
            j += 1

    while (i <= q):
        tmp[t] = nums[i]
        t += 1
        i += 1

    while (j <= e):
        tmp[t] = nums[j]
        t += 1
        j += 1

    i = s
    t = 0
    while (i <= e):
        nums[i] = tmp[t]
        cnt += 1
        if cnt == K:
            result = tmp[t]
            break
        t += 1
        i += 1



def merge_sort(arr, s, e):
    if cnt > K:
        return

    if (s < e):
        q = (s + e) // 2
        merge_sort(arr, s, q)
        merge_sort(arr, q+1, e)
        merge(arr, s, q, e)


N, K = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
result = -1

merge_sort(nums, 0, N-1)

print(result)