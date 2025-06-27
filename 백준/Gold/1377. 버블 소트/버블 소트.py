# 정렬 전 인덱스와 정렬 후 인덱스의 차이 중 가장 큰 값이 답이 됨
import sys
input = sys.stdin.readline
N = int(input())
nums = []

for i in range(N):
    num = int(input())
    nums.append((num, i))

sorted_nums = sorted(nums)
answer = 0

for i in range(N):
    tmp = sorted_nums[i][1] - i
    answer = max(tmp, answer)

print(answer + 1)