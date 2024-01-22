N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
for i in range(1, (1 << N)): # N에 해당하는 값은 (1 << N) - 1 인데 range는 마지막 값-1이니깐 구간 (1<<N). 그리고 크기가 양수라고 했으니깐 공집합 제외하기 위해서 1부터
    sum = 0
    for j in range(N):
        if i & (1<<j):
            sum += nums[j]
    if sum == S:
        ans += 1
print(ans)