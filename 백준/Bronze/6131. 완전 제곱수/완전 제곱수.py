N = int(input())
ans = []
for a in range(1, 501):
    for b in range(1, a):
        if (a+b) * (a-b) == N:
            ans.append((a, b))
print(len(ans))