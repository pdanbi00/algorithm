N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def dfs():
    if len(ans) == M:
        print(*ans)
        return
    check = 0
    for i in range(N):
        if check != nums[i] and visited[i] == 0:
            ans.append(nums[i])
            visited[i] = 1
            check = nums[i]
            dfs()
            ans.pop()
            visited[i] = 0

visited = [0] * N

dfs()