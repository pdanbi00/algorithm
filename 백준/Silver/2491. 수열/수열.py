N = int(input())
nums = list(map(int, input().split()))
ans = 0
stack = []

for i in range(N):
    if not stack:
        stack.append(nums[i])
    else:
        if stack[-1] <= nums[i]:
            stack.append(nums[i])
        else:
            ans = max(ans, len(stack))
            stack = [nums[i]]
ans = max(ans, len(stack))

stack = []
for i in range(N):
    if not stack:
        stack.append(nums[i])
    else:
        if stack[-1] >= nums[i]:
            stack.append(nums[i])
        else:
            ans = max(ans, len(stack))
            stack = [nums[i]]
ans = max(ans, len(stack))
print(ans)