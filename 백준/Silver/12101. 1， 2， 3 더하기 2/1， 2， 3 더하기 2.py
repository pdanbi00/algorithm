N, K = map(int, input().split())
cnt = 0
ans = ''

def func(line, total):
    global cnt, ans
    if total == N:
        cnt += 1
        if cnt == K:
            ans = line
        return

    for i in range(1, 4):
        if total + i <= N:
            func(line + str(i), total + i)


func('', 0)
# print(ans)
if cnt < K:
    print(-1)
else:
    tmp = '+'.join(ans)
    print(tmp)