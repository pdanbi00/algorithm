def check(num):
    total = 0
    for i in range(N-1):
        total += abs(num[i] - num[i+1])
    return total

def func(index, num):
    global ans
    if index == N:
        temp = check(num)
        ans = max(ans, temp)
    for i in range(N):
        if not used[i]:
            used[i] = True
            func(index+1, num+[nums[i]])
            used[i] = False


N = int(input())
nums = list(map(int, input().split()))
used = [False] * N
ans = -100000
nums.sort()
func(0, [])
print(ans)