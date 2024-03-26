ans = 0
total = 0
for i in range(4):
    off, on = map(int, input().split())
    total += on
    total -= off
    if total > ans:
        ans = total
print(ans)