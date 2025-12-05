A, K = map(int, input().split())
cnt = 0

while K != A:
    isChanged = False
    if K - 1 == A:
        cnt += 1
        break

    if K % 2 == 1:
        K -= 1
        cnt += 1
        isChanged = True
    else:
        while K % 2 == 0:
            if K - 1 == A or K // 2 < A:
                break

            K //= 2
            cnt += 1
            isChanged = True

    if not isChanged:
        cnt += (K-A)
        break

print(cnt)