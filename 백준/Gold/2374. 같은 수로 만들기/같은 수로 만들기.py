N = int(input())
stack = []
ans = 0
max_v = 0
for _ in range(N):
    n = int(input())
    max_v = max(n, max_v)
    if stack:
        if stack[-1] < n:
            ans += n - stack.pop()
            stack.append(n)
        else:
            stack.pop()
            stack.append(n)
    else:
        stack.append(n)

while stack:
    ans += max_v - stack.pop()

print(ans)
