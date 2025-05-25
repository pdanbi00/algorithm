N = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9
ans_list = []

def dfs(idx, a, b, c, d, price, pick):
    global answer, arr

    if idx == N:
        if a >= mp and b >= mf and c >= ms and d >= mv:
            if price <= answer:
                answer = price
                ans_list.append(pick)
        return
    dfs(idx+1, a, b, c, d, price, pick)
    dfs(idx+1, a + nutrients[idx][0], b + nutrients[idx][1], c + nutrients[idx][2], d + nutrients[idx][3], price + nutrients[idx][4], pick + [idx+1])


dfs(0, 0, 0, 0, 0, 0, [])

if answer == 1e9:
    print(-1)
else:
    ans_list.sort()
    print(answer)
    print(*ans_list[0])
