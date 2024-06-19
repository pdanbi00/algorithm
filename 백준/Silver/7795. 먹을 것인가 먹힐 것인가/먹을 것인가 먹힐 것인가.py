# A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    start = 0
    ans = 0

    for i in range(N):
        while True:
            if start == M or A[i] <= B[start]:
                ans += start
                break
            else:
                start += 1

    print(ans)