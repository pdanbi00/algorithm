A, B = map(int, input().split())
if A > B:
    B, A = A, B
cnt = 0
ans = []
for i in range(A+1, B):
    cnt += 1
    ans.append(i)
print(cnt)
print(*ans)