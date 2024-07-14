N = int(input())
ans = 0
for _ in range(N):
    words = list(input())
    arr = []
    for w in words:
        if arr and arr[-1] == w:
            arr.pop()
        else:
            arr.append(w)
    if len(arr) == 0:
        ans += 1
print(ans)