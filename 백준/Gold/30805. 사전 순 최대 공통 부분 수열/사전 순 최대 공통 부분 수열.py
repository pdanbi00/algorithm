N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

idx_A = 0
idx_B = 0

ans = []

while idx_A < N and idx_B < M:
    result = -1
    for i in range(idx_A, N):
        for j in range(idx_B, M):
            if A[i] == B[j]:
                result = max(result, A[i])

    if result != -1:
        ans.append(result)
        while A[idx_A] != result:
            idx_A += 1

        while B[idx_B] != result:
            idx_B += 1

        idx_A += 1
        idx_B += 1
    else:
        break

print(len(ans))
print(*ans)