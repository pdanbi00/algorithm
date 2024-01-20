def func(index, perm):
    global min_cost
    if index == N:
        ans = 0
        for i in range(N-1):
            if cost[perm[i]][perm[i+1]] == 0:
                return
            ans += cost[perm[i]][perm[i+1]]
        if cost[perm[N-1]][perm[0]] == 0:
            return
        ans += cost[perm[N-1]][perm[0]]
        min_cost = min(ans, min_cost)
        return
    for i in range(1, N):
        if not used[i]:
            used[i] = True
            func(index+1, perm + [nums[i]])
            used[i] = False


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
used = [False] * N
min_cost = 9999999999999999999
nums = [i for i in range(N)]
func(1, [0])
print(min_cost)