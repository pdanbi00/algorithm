N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = set()

def dfs(idx, n, total):
    if idx == M:
        ans.add(tuple(total))
        return

    for j in range(n, N):
        total.append(nums[j])
        dfs(idx+1, j+1, total)
        total.pop()

for i in range(N):
    dfs(1, i+1, [nums[i]])

ans = list(ans)
ans.sort()

for i in range(len(ans)):
    print(*ans[i])