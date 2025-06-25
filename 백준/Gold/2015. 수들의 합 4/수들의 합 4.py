N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums_sum = [0] * (N+1)
for i in range(N):
    nums_sum[i+1] = nums_sum[i] + nums[i]

answer = 0
num_dict = dict()

# i부터 j까지의 합 : nums_sum[j] - nums_sum[i-1] = K
# nums_sum[j] - K = nums_sum[i-1]
for j in range(1, N+1):
    if nums_sum[j] == K:
        answer += 1

    if nums_sum[j] - K in num_dict:
        answer += num_dict[nums_sum[j]-K]

    if nums_sum[j] in num_dict:
        num_dict[nums_sum[j]] += 1
    else:
        num_dict[nums_sum[j]] = 1

print(answer)