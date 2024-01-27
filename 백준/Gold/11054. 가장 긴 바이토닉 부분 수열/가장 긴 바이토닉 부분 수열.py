N = int(input())
nums = list(map(int, input().split()))
dp_1 = [0] * N # 증가하는 가장 긴 수열 담을 dp
dp_2 = [0] * N # 감소하는 가장 긴 수열 담을 dp
ans = [0] * N
# 증가하는 가장 긴 수열 길이 구하기
for i in range(N):
    dp_1[i] = 1
    for j in range(i):
        if nums[i] > nums[j] and dp_1[i] < dp_1[j] + 1:
            dp_1[i] = dp_1[j] + 1

# 감소하는 가장 긴 수열 길이 구하기
for i in range(N-1, -1, -1):
    dp_2[i] = 1
    for j in range(i+1, N):
        if nums[i] > nums[j] and dp_2[i] < dp_2[j] + 1:
            dp_2[i] = dp_2[j] + 1
for i in range(N):
    ans[i] = dp_1[i] + dp_2[i] - 1
print(max(ans))