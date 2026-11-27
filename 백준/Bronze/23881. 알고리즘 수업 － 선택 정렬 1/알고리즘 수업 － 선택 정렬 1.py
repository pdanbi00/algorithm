N, K = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
answer = [-1]
for i in range(N-1, 0, -1):
    max_num = nums[i]
    idx = -1
    for j in range(i):
        if max_num < nums[j]:
            max_num = nums[j]
            idx = j
    if idx != -1:
        cnt += 1
        if cnt == K:
            answer = [nums[i], nums[idx]]
            break
        nums[i], nums[idx] = nums[idx], nums[i]

print(*answer)