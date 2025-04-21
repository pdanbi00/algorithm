N = int(input())
idx = list(map(int, input().split()))
ans = []
for i in range(1, N+1):
    ans.insert(i-1-idx[i-1], i)
print(*ans)