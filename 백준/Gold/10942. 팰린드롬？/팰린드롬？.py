import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[False] * N for _ in range(N)]
# dp[i][j] : i번째부터 j번째까지 수가 팰린드롬인지 아닌지

# 모든 길이가 1인 부분 문자열은 팰린드롬
for i in range(N):
    dp[i][i] = True
# 길이가 2일때 두개가 같으면 팰린드롬
for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = True

# 길이가 3 이상인 부분 문자열에 대해서
for length in range(3, N+1):
    for i in range(N - (length - 1)):
        j = i + length - 1
        if nums[i] == nums[j] and dp[i+1][j-1]:
        # 첫번째 숫자랑 마지막 숫자가 같고 그 사이 숫자들 dp 확인하면 됨
            dp[i][j] = True

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if dp[S-1][E-1]:
        print(1)
    else:
        print(0)