nums = []

def make_num(idx, n):
    if idx == 0:
        nums.append(int(n))
        return
    target = int(n[-1])
    for i in range(target):
        make_num(idx-1, n + str(i))

for i in range(11):
    for k in range(10):
        make_num(i, str(k))

N = int(input())
if N >= len(nums):
    print(-1)
else:
    print(nums[N])