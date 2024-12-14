N, M = map(int, input().split())
arr = []
for _ in range(N):
    p, l = map(int, input().split())
    miles = list(map(int, input().split()))
    miles.sort(reverse=True)
    if p >= l:
        arr.append(miles[l-1])
    else:
        arr.append(1)

arr.sort()
total = 0
ans = 0
for i in range(N):
    total += arr[i]
    if total > M:
        break
    else:
        ans += 1
print(ans)
