# A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    ans = 0
    for i in range(N):
        cnt = 0
        if A[i] <= B[0]:
            break
        for j in range(M):
            if A[i] > B[j]:
                cnt += 1
            else:
                break
        ans += cnt
    print(ans)