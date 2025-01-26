N = int(input())
eggs = []
for _ in range(N):
    strong, weight = map(int, input().split())
    eggs.append([strong, weight])

ans = 0

def check(eggs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0:
            cnt += 1
    return cnt

def dfs(depth, arr):
    global ans
    if depth == N:
        ans = max(ans, check(arr))
        return

    # 현재 들고 있는 계란이 깨져있을 경우
    if arr[depth][0] <= 0:
        dfs(depth+1, arr)
    else:
        isBroken = True
        for i in range(N):
            if depth != i and arr[i][0] > 0:
                isBroken = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                dfs(depth+1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if isBroken:
            dfs(N, arr)

dfs(0, eggs)
print(ans)
