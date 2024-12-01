N = int(input())
nums = list(map(int, input().split()))
calc = list(map(int, input().split()))

min_ans = 10000000000000
max_ans = -100000000000000

def dfs(n, temp):
    global max_ans, min_ans

    # 종료조건
    if n == N-1:
        min_ans = min(min_ans, temp)
        max_ans = max(max_ans, temp)
        return

    if calc[0] != 0: # 덧셈
        calc[0] -= 1
        dfs(n+1, temp + nums[n+1])
        calc[0] += 1

    if calc[1] != 0: # 뺄셈
        calc[1] -= 1
        dfs(n+1, temp - nums[n+1])
        calc[1] += 1

    if calc[2] != 0: # 곱셈
        calc[2] -= 1
        dfs(n+1, temp * nums[n+1])
        calc[2] += 1

    if calc[3] != 0: # 나눗셈
        calc[3] -= 1
        if temp < 0 and nums[n+1] > 0:
            dfs(n+1, -(abs(temp) // nums[n+1]))
        else:
            dfs(n+1, temp // nums[n+1])
        calc[3] += 1
dfs(0, nums[0])
print(max_ans)
print(min_ans)