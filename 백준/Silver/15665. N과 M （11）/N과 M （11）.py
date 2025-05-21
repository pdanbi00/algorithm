N, M = map(int, input().split())
nums = list(map(int, input().split()))
# nums.sort()

answer = set()

def func(idx, temp):
    if idx == M:
        answer.add(tuple(temp))
        return

    for i in range(N):
        temp[idx] = nums[i]
        func(idx+1, temp)
        temp[idx] = -1

temp = [-1] * M
func(0, temp)

answer = list(answer)
answer.sort()
for i in range(len(answer)):
    print(*answer[i])
