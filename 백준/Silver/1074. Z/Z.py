# 시간 초과
# def solve(n, r, c):
#     global number
#     num = n - 1
#     if num == 0:
#         for dr, dc in ((0, 0), (0, 1), (1, 0), (1, 1)):
#             nr = r + dr
#             nc = c + dc
#             arr[nr][nc] = number
#             number += 1
#         return
#     else:
#         for dr, dc in ((0, 0), (0, 2**num), (2**num, 0), (2**num, 2**num)):
#             solve(num, r+dr, c+dc)

N, r, c = map(int, input().split())
# arr = [[0] * (2**N) for _ in range (2**N)]
# number = 0
ans = 0
while N > 0:
    N -= 1
    # 왼위
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0
    # 오위
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= 2 ** N
    # 왼아래
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= 2 ** N
    # 오아래
    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= 2 ** N
        c -= 2 ** N
print(ans)
