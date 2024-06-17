N = int(input())
nums = list(map(int, input().split()))

start = 0
answer = 0
end = 0
visited = [False] * 100001 # 수열 중복 없애기 위해서 수열에 각 숫자가 포함되어있는지 체크

while start <= end and end < N:
    if not visited[nums[end]]:
        visited[nums[end]] = True
        answer += (end - start + 1)
        end += 1
    else:
        visited[nums[start]] = False
        start += 1

print(answer)
