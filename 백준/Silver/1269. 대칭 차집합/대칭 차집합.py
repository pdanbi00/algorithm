a_cnt, b_cnt = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

nums = dict()

for i in range(a_cnt):
    if A[i] in nums:
        nums[A[i]] += 1
    else:
        nums[A[i]] = 1

for i in range(b_cnt):
    if B[i] in nums:
        nums[B[i]] += 1
    else:
        nums[B[i]] = 1

answer = 0
for k, v in nums.items():
    if v == 1:
        answer += 1

print(answer)