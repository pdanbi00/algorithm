# LIS. 가장긴 증가하는 부분 수열. 근데 DP로 풀면 n^2가 걸리는데 n이 10만이라서 안됨
# -> 이분탐색으로 해야됨
import bisect
N = int(input())
lines = list(map(int, input().split()))

result = [lines[0]]
for i in range(1, N):
    index = bisect.bisect_left(result, lines[i])
    if index == len(result):
        result.append(lines[i])
    else:
        result[index] = lines[i]
print(N-len(result))