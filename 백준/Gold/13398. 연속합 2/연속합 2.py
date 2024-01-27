N = int(input())
nums = list(map(int, input().split()))
dp_1 = [0] * N # dp_1[i]는 nums[i]로 끝나는 연속된 수의 가장 큰 합
dp_2 = [0] * N # dp_2[i]는 nums[i]로 시작하는 연속된 수의 가장 큰 합
dp_1[0] = nums[0]
for i in range(1, N):
    dp_1[i] = max(dp_1[i-1] + nums[i], nums[i])
dp_2[N-1] = nums[-1]
for i in range(N-2, -1, -1):
    dp_2[i] = max(dp_2[i+1] + nums[i], nums[i])
ans = max(dp_1)
for i in range(1, N-1):
    if dp_1[i-1] + dp_2[i+1] > ans:
        ans = dp_1[i-1] + dp_2[i+1]
print(ans)