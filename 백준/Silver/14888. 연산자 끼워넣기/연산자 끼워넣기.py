N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_ans = 1000000000
max_ans = -1000000000

def dfs(n, temp):
    global min_ans, max_ans

    # 종료조건
    if n == N-1:
        min_ans = min(min_ans, temp)
        max_ans = max(max_ans, temp)
        return

    if operators[0] != 0: # 덧셈
        operators[0] -= 1
        dfs(n+1, temp + nums[n+1])
        operators[0] += 1

    if operators[1] != 0: # 뺄셈
        operators[1] -= 1
        dfs(n+1, temp - nums[n+1])
        operators[1] += 1

    if operators[2] != 0: # 곱셈
        operators[2] -= 1
        dfs(n+1, temp * nums[n+1])
        operators[2] += 1

    if operators[3] != 0: # 나눗셈
        operators[3] -= 1
        if temp < 0 and nums[n+1] > 0:
            dfs(n+1, -(abs(temp) // nums[n+1]))
        else:
            dfs(n+1, temp // nums[n+1])
        operators[3] += 1

dfs(0, nums[0])
print(max_ans)
print(min_ans)