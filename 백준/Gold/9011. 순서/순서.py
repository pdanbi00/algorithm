import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    possible = True
    ans = [0] * N
    used = [R[N-1] + 1]
    ans[-1] = R[N-1] + 1
    for i in range(N-2, -1, -1):
        res = R[i] + 1
        used.sort()
        for j in used:
            if res >= j:
                res += 1
            else:
                break

        if res > N:
            possible = False
            break
        ans[i] = res
        used.append(res)

    if possible:
        print(*ans)
    else:
        print("IMPOSSIBLE")