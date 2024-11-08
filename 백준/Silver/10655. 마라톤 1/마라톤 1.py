N = int(input())
total = 0
p_r, p_c = map(int, input().split())
arr = [(p_r, p_c)]
for _ in range(N-1):
    r, c = map(int, input().split())
    total += abs(p_r - r) + abs(p_c - c)
    arr.append((r, c))
    p_r, p_c = r, c
ans = 1e9

for i in range(1, N-1):
    tmp = total
    tmp -= (abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1]))
    tmp -= (abs(arr[i][0] - arr[i + 1][0]) + abs(arr[i][1] - arr[i + 1][1]))
    tmp += (abs(arr[i+1][0] - arr[i-1][0]) + abs(arr[i+1][1] - arr[i-1][1]))
    ans = min(ans, tmp)
print(ans)