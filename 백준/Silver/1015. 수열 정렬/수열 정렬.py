N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

p = []
for i in range(N):
    p.append(sorted_nums.index(nums[i]))
    # 같은 숫자가 여러개 있을 경우 중복 방지하기 위해서
    sorted_nums[sorted_nums.index(nums[i])] = -1

print(*p)