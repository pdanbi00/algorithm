max = 0
for i in range(1, 6):
    arr = list(map(int, input().split()))
    total = 0
    for j in range(4):
        total += arr[j]
    if total > max:
        max = total
        ans = i
print(ans, max)