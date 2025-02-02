N = int(input())
open1, open2 = map(int, input().split())
M = int(input())
order = list(int(input()) - 1 for _ in range(M))

door = [1] * N
door[open1-1] = 0
door[open2-1] = 0

ans = 1e9

def go(x, cnt, arr):
    global ans
    if x == M:
        ans = min(ans, cnt)
        return
    cur = order[x] # 현재위치
    # 왼쪽으로 찾기
    for i in range(cur, -1, -1):
        if arr[i] == 0:
            tmp = arr[:]
            tmp[i], tmp[cur] = tmp[cur], tmp[i]
            go(x+1, cnt + abs(cur - i), tmp)

    # 오른쪽으로 찾기
    for i in range(cur+1, N):
        if arr[i] == 0:
            tmp = arr[:]
            tmp[i], tmp[cur] = tmp[cur], tmp[i]
            go(x+1, cnt + abs(cur - i), tmp)

go(0, 0, door)
print(ans)
