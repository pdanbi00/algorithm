x, y, w, h = map(int, input().split())
if x > w and y > h:
    ans = (x-w) (y-h)
else:
    ans = min(abs(w-x), abs(x-0), abs(h-y), abs(y-0))
print(ans)