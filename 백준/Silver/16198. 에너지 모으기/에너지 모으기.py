N = int(input())
goosle = list(map(int, input().split()))

ans = -1

used = [False] * N

def dfs(idx, total):
    global ans
    if idx == N-2:
        ans = max(ans, total)
        return
    for i in range(1, N-1):
        if not used[i]:
            # i번째보다 앞에 있는 살아있는 구슬 찾기
            for j in range(i-1, -1, -1):
                if not used[j]:
                    a = goosle[j]
                    break
            # i번째보다 뒤에 있는 살아있는 구슬 찾기
            for j in range(i+1, N):
                if not used[j]:
                    b = goosle[j]
                    break

            used[i] = True
            dfs(idx+1, total+(a*b))
            used[i] = False

dfs(0, 0)
print(ans)